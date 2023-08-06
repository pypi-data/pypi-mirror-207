import pandas as pd
import numpy as np


####################################################
# ta3: standard technical library
####################################################
# lv0
####################################################


def hhv(S, W):
    # 窗口期W内S的MAX
    if isinstance(W, int):
        return S.rolling(W).max()

    _S = np.array(S)
    _W = np.array(W.fillna(0))
    _max = np.full((len(_S),), np.nan)

    for i in range(len(_W)):
        start = int(i + 1 - _W[i])
        start = start if start >= 0 else 0
        _max[i] = _S[i] if start == i + 1 else np.max(_S[start:i + 1])

    return pd.Series(_max, index=S.index, name=S.name)


def llv(S, W):
    # 窗口期W内S的MIN
    if isinstance(W, int):
        return S.rolling(W).min()

    _S = np.array(S)
    _W = np.array(W.fillna(0).astype(int))
    _min = np.full((len(_S),), np.nan)

    for i in range(len(_W)):
        start = int(i + 1 - _W[i])
        start = start if start >= 0 else 0
        _min[i] = _S[i] if start == i + 1 else np.min(_S[start:i + 1])

    return pd.Series(_min, index=S.index, name=S.name)


def ref(S, W):
    # S.shift(W)
    if isinstance(W, int):
        return S.shift(W)

    _S = np.array(S)
    _W = np.array(W.fillna(0).astype(int))
    output = np.full((len(_S),), np.nan)

    for i in range(len(_W)):
        start = int(i - _W[i])
        if start < 0:
            output[i] = np.nan
            continue
        output[i] = _S[start]

    return pd.Series(output, index=S.index, name=S.name)


def last(S, A, B):
    # 从前A日到前B日一直满足S_BOOL条件, 要求A>B & A>0 & B>=0
    return pd.Series(S).rolling(A + 1).apply(lambda x: np.all(x[::-1][B:]), raw=True).astype(float)


def cross(S1, S2):
    # 判断向上金叉穿越
    return ((S1 > S2) & (S1 <= S2).shift(1)).astype(float)


def long_cross(S1, S2, window=10):
    # 两条线维持一定周期后交叉,S1在N周期内都小于S2,本周期从S1下方向上穿过S2时返回1,否则返回0
    # window=1时等同于cross(S1, S2)
    return (last(S1 <= S2, window, 1).astype(bool) & (S1 > S2)).astype(float)


def bars_last(S):
    # 上一次条件S成立到当前的周期
    M = np.concatenate(([0], np.where(S, 1, 0)))
    for i in range(1, len(M)):
        M[i] = 0 if M[i] else M[i - 1] + 1
    M = pd.Series(M[1:], index=S.index, name=S.name)
    return M


def bars_last_count(S):
    # 统计连续满足S条件的周期数
    # bars_last_count(CLOSE>OPEN)表示统计连续收阳的周期数
    rt = np.zeros(len(S) + 1)
    for i in range(len(S)):
        rt[i + 1] = rt[i] + 1 if S[i] else rt[i + 1]
    rt = pd.Series(rt[1:], index=S.index, name=S.name)
    return rt


def bars_since(S, N):
    # N周期内第一次S条件成立到现在的周期数, N为常量
    return pd.Series(S).rolling(N).apply(lambda x: N - 1 - np.argmax(x) if np.argmax(x) or x[0] else 0, raw=True)


def value_when(S, X):
    # 当S条件成立时,取X的当前值,否则取value_when的上个成立时的X值
    output = S.copy()
    output[:] = pd.Series(np.where(S, X, np.nan)).ffill()
    return output


def top_range(S):
    # top_range(HIGH)表示当前最高价是近多少周期内最高价的最大值
    return S.expanding(2).apply(lambda x: np.argmin(np.flipud(x[:-1] <= x[-1]).astype(float)), raw=True)


def low_range(S):
    # low_range(LOW)表示当前最低价是近多少周期内最低价的最小值
    return S.expanding(2).apply(lambda x: np.argmin(np.flipud(x[:-1] >= x[-1]).astype(float)), raw=True)


def sum_bars(S, A):
    # 回推累加直到大于等于A的bar数
    # 注意：S中元素只能为非负
    _S = np.array(S.fillna(0))
    _S = np.flipud(_S)
    length = len(_S)

    #
    if isinstance(A * 1.0, float):
        _A = np.repeat(A, length)
    else:
        _A = np.array(A.fillna(0))

    #
    _A = np.flipud(_A)
    sumbars = np.full((length,), np.nan)
    cumsum = np.insert(np.cumsum(_S), 0, 0.0)  # 已知为ascending序列

    #
    for i in range(length):
        pos = np.searchsorted(cumsum[i + 1:] - cumsum[i], _A[i], side='left')
        if pos < length - i:
            sumbars[i] = pos + 1.0

    return pd.Series(np.flipud(sumbars), index=S.index, name=S.name)


####################################################
# lv1
####################################################
def is_up_deviation(price, indicator, up_cond, down_cond):
    # 判断price, indicator走势是否出现顶背离
    # up_cond: 上升段开始点（是则为1，否则为0）
    # down_cond: 下降段开始点（是则为1，否则为0）
    end_n1 = sum_bars(down_cond, 1)
    range_n1 = sum_bars(ref(up_cond, end_n1), 1)  # 上一段上升段长度
    end_n2 = sum_bars(down_cond, 2)
    range_n2 = sum_bars(ref(up_cond, end_n2), 1)  # 上上一段上升段长度
    #
    hh1 = hhv(ref(price, end_n1), range_n1)
    hh2 = hhv(ref(price, end_n2), range_n2)
    #
    ind1 = hhv(ref(indicator, end_n1), range_n1)
    ind2 = hhv(ref(indicator, end_n2), range_n2)
    # 价格创新高，指标未创新高，且此时处于下跌趋势内
    output = ((ind1 < ind2) & (hh1 > hh2) & (sum_bars(up_cond, 1) > end_n1)).astype(float)
    output[np.isnan(price * indicator)] = np.nan
    return output


def is_down_deviation(price, indicator, up_cond, down_cond):
    # 判断price, indicator走势是否出现顶背离
    # up_cond: 上升段开始点（是则为1，否则为0）
    # down_cond: 下降段开始点（是则为1，否则为0）
    end_n1 = sum_bars(up_cond, 1)
    range_n1 = sum_bars(ref(down_cond, end_n1), 1)  # 上一段下跌段长度
    end_n2 = sum_bars(up_cond, 2)
    range_n2 = sum_bars(ref(down_cond, end_n2), 1)  # 上上一段下跌段长度
    #
    ll1 = llv(ref(price, end_n1), range_n1)
    ll2 = llv(ref(price, end_n2), range_n2)
    #
    ind1 = llv(ref(indicator, end_n1), range_n1)
    ind2 = llv(ref(indicator, end_n2), range_n2)
    # 价格创新低，指标未创新低，且此时处于上涨趋势内
    output = ((ind1 > ind2) & (ll1 < ll2) & (end_n1 < sum_bars(down_cond, 1))).astype(float)
    output[np.isnan(price * indicator)] = np.nan
    return output
