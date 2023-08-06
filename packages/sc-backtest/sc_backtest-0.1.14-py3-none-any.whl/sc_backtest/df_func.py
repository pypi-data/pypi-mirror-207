import pandas as pd
import numpy as np
from sc_backtest import ta, ta2
from copy import copy


###########################
# input: np.array
# output: np.array
###########################
# 非参数算子
###########################
#
def df_add(x, y):
    return x + y


#
def df_sub(x, y):
    return x - y


#
def df_mult(x, y):
    return x * y


#
def df_divide(x, y):
    temp = copy(y)
    temp[np.isclose(temp, 0.0)] = np.nan
    return x / temp


#
def df_sign(x):
    return np.sign(x)


#
def df_abs(x):
    return np.abs(x)


#
def df_square(x):
    return np.square(x)


#
def df_gap_ratio(x, y):
    return (x - y)/(np.abs(x) + np.abs(y))


###########################
# 单输入单参数算子
###########################
#
def df_shift(window):
    def _shift(x):
        return pd.DataFrame(x).shift(window)

    _shift.__name__ = f'df_shift_{int(window)}'
    return _shift


#
def df_diff(window):
    def _diff(x):
        return pd.DataFrame(x).diff(window)

    _diff.__name__ = f'df_diff_{int(window)}'
    return _diff


#
def df_acc(window):
    def _acc(x):
        return pd.DataFrame(x).diff(window).diff(window)

    _acc.__name__ = f'df_acc_{int(window)}'
    return _acc


#
def df_mean(window):
    def _mean(x):
        return pd.DataFrame(x).rolling(window).mean()

    _mean.__name__ = f'df_mean_{int(window)}'
    return _mean


#
def df_std(window):
    def _std(x):
        return pd.DataFrame(x).rolling(window).std()

    _std.__name__ = f'df_std_{int(window)}'
    return _std


#
def df_ema(window):
    def _ema(x):
        return pd.DataFrame(x).ewm(span=window, adjust=False).mean()

    _ema.__name__ = f'df_ema_{int(window)}'
    return _ema


#
def df_rank(window):
    def _rank(x):
        return pd.DataFrame(x).rolling(window).apply(lambda m: (m.rank(method='min',
                                                                       ascending=True).iloc[-1] - 1) / (
                                                                       window - 1) - 0.5)

    _rank.__name__ = f'df_rank_{int(window)}'
    return _rank


#
def df_z_score(window):
    def _z_score(x):
        temp = pd.DataFrame(x)
        return (temp - temp.rolling(window).mean()) / temp.rolling(window).std()

    _z_score.__name__ = f'df_z_score_{int(window)}'
    return _z_score


#
def df_ez_score(window):
    def _ez_score(x):
        return (x - pd.DataFrame(x).ewm(span=window, adjust=False).mean())/pd.DataFrame(x).ewm(span=window, adjust=False).std()

    _ez_score.__name__ = f'df_ez_score_{int(window)}'
    return _ez_score


#
def df_max(window):
    def _max(x):
        return pd.DataFrame(x).rolling(window).max()

    _max.__name__ = f'df_max_{int(window)}'
    return _max


#
def df_min(window):
    def _min(x):
        return pd.DataFrame(x).rolling(window).min()

    _min.__name__ = f'df_min_{int(window)}'
    return _min


#
def df_median(window):
    def _median(x):
        return pd.DataFrame(x).rolling(window).median()

    _median.__name__ = f'df_median_{int(window)}'
    return _median


#
def df_rsi(window):
    def _rsi(x):
        temp = pd.DataFrame(x)
        U = temp.diff()
        U[U < 0] = 0
        D = temp.diff()
        D[D > 0] = 0
        D = D.abs()

        def _smma(s, w):
            return s.ewm(alpha=1 / w, adjust=False, min_periods=int(w + 20)).mean()

        RS = _smma(U, window) / _smma(D, window)

        return -100 / (1 + RS) + 100 - 50

    _rsi.__name__ = f'df_rsi_{int(window)}'
    return _rsi


#
def df_hl(window):
    def _hl(x):
        temp = pd.DataFrame(x)
        rolling_max = temp.rolling(window).max()
        rolling_min = temp.rolling(window).min()
        return (temp - rolling_min) / (rolling_max - rolling_min) - 0.5

    _hl.__name__ = f'df_hl_{int(window)}'
    return _hl


#
def df_de_mean(window):
    def _de_mean(x):
        temp = pd.DataFrame(x)
        return temp - temp.rolling(window).mean()

    _de_mean.__name__ = f'df_de_mean_{int(window)}'
    return _de_mean


#
def df_div_std(window):
    def _div_std(x):
        temp = pd.DataFrame(x)
        return temp / temp.rolling(window).std()

    _div_std.__name__ = f'df_div_std_{int(window)}'
    return _div_std


#
def df_mean_std(window):
    def _mean_std(x):
        temp = pd.DataFrame(x)
        return temp.rolling(window).mean() / temp.rolling(window).std()

    _mean_std.__name__ = f'df_mean_std_{int(window)}'
    return _mean_std


#
def df_sim_yoy(window):
    def _sim_yoy(x):
        temp = pd.DataFrame(x)
        return (temp - temp.shift(window)) / ((temp.abs() + temp.shift(window).abs()) / 2)

    _sim_yoy.__name__ = f'df_sim_yoy_{int(window)}'
    return _sim_yoy


#
def df_sma_deviation(window):
    def _sma_deviation(x):
        temp = pd.DataFrame(x)
        temp_mean = temp.rolling(window).mean()
        temp_mean[np.isclose(temp_mean, 0.0)] = np.nan
        return temp / temp_mean - 1.0

    _sma_deviation.__name__ = f'df_sma_deviation_{int(window)}'
    return _sma_deviation


#
def df_slope(window):
    def _slope(x):
        _x = pd.DataFrame(x)
        _diff = _x.diff(1)
        return _diff.ewm(span=window - 1, adjust=False).mean() - _x.diff(window - 1) / (window - 1)

    _slope.__name__ = f'df_slope_{int(window)}'
    return _slope


#
def df_convexity(window):
    def _convexity(x):
        _x = pd.DataFrame(x)
        k = (_x - _x.shift(window - 1)) / (window - 1)

        temp1 = (0.5 * window * (window - 1)) * k + _x.shift(window - 1) * window
        temp2 = _x.rolling(window).sum()

        return (temp1 - temp2) / window

    _convexity.__name__ = f'df_convexity_{int(window)}'
    return _convexity


#
def df_above_mean(window):
    def _above_mean(x):
        _x = pd.DataFrame(x)
        return _x.rolling(window).apply(lambda m: np.count_nonzero(m > m.mean()) / window - 0.5, raw=True)

    _above_mean.__name__ = f'df_above_mean_{int(window)}'
    return _above_mean


#
def df_below_mean(window):
    def _below_mean(x):
        _x = pd.DataFrame(x)
        return _x.rolling(window).apply(lambda m: np.count_nonzero(m < m.mean()) / window - 0.5, raw=True)

    _below_mean.__name__ = f'df_below_mean_{int(window)}'
    return _below_mean


#
def df_max_min_gap(window):
    def _max_min_gap(x):
        temp = pd.DataFrame(x)
        _max = temp.rolling(window).max()
        _min = temp.rolling(window).min()
        _gap = (_max - _min).abs()
        _gap[np.sign(_max) != np.sign(_min)] = _max - _min
        return (_gap/(_max.abs() + _min.abs()))

    _max_min_gap.__name__ = f'df_max_min_gap_{int(window)}'
    return _max_min_gap

###########################
# 单输入双参数算子
###########################
def df_z_score_clip(window, threshold=3):
    def _inner_func(x):
        pass

    _inner_func.__name__ = f'df_z_score_clip_{int(window)}_{int()}'
    return _inner_func


#
def df_shift_corr(window, window2):
    def _shift_corr(x):
        temp = pd.DataFrame(x)
        return temp.rolling(window + window2).apply(lambda m: np.corrcoef(m[:-window2],
                                                                          m[window2:])[0, 1], raw=True)

    _shift_corr.__name__ = f'df_shift_corr_{int(window)}'
    return _shift_corr


###########################
# 双输入单参数算子
###########################
def df_pair_corr(window):
    def _pair_corr(x, y):
        temp = pd.DataFrame(y)
        return pd.DataFrame(x).rolling(window).corr(temp)

    _pair_corr.__name__ = f'df_pair_corr_{int(window)}'
    return _pair_corr


def df_r_square(window):
    def _r_square(x, y):
        temp = pd.DataFrame(y)
        return np.square(pd.DataFrame(x).rolling(window).corr(temp))

    _r_square.__name__ = f'df_r_square_{int(window)}'
    return _r_square


def df_residual(window):
    def _residual(x, y):
        _x = pd.DataFrame(x)
        _y = pd.DataFrame(y)
        x_mean = _x.rolling(window).mean()
        y_mean = _y.rolling(window).mean()
        x_var = _x.rolling(window).var()
        x_y_cov = _x.rolling(window).cov(_y)
        #
        _beta = x_y_cov / x_var
        _alpha = y_mean - x_mean * _beta
        return _y - (_alpha + _beta * _x)

    _residual.__name__ = f'df_residual_{int(window)}'
    return _residual


def df_beta(window):
    def _beta(x, y):
        _x = pd.DataFrame(x)
        _y = pd.DataFrame(y)
        x_var = _x.rolling(window).var()
        x_y_cov = _x.rolling(window).cov(_y)

        return x_y_cov / x_var

    _beta.__name__ = f'df_beta_{int(window)}'
    return _beta


def df_alpha(window):
    def _alpha(x, y):
        _x = pd.DataFrame(x)
        _y = pd.DataFrame(y)
        x_mean = _x.rolling(window).mean()
        y_mean = _y.rolling(window).mean()
        x_var = _x.rolling(window).var()
        x_y_cov = _x.rolling(window).cov(_y)
        #
        _beta = x_y_cov / x_var
        return y_mean - x_mean * _beta

    _alpha.__name__ = f'df_alpha_{int(window)}'
    return _alpha


def df_standard_diff(window):
    def _standard_diff(x, y):
        return df_hl(window)(x) - df_hl(window)(y)

    _standard_diff.__name__ = f'df_standard_diff_{int(window)}'
    return _standard_diff


###########################
# 单输入双参数算子
###########################
def df_gap_z_score(window1, window2):
    def _gap_z_score(x):
        temp = pd.DataFrame(x)
        return temp.rolling(window1 * window2).apply(lambda m: (m[-1] -
                                                                np.nanmean(m[-1::-window2]))/np.nanstd(m[-1::-window2]),
                                                     raw=True)

    _gap_z_score.__name__ = f'df_gap_z_score_{int(window1)}_{int(window2)}'
    return _gap_z_score


def df_gap_mean(window1, window2):
    def _gap_mean(x):
        temp = pd.DataFrame(x)
        return temp.rolling(window1 * window2).apply(lambda m: np.nanmean(m[-1::-window2]), raw=True)

    _gap_mean.__name__ = f'df_gap_mean_{int(window1)}_{int(window2)}'
    return _gap_mean


def df_gap_std(window1, window2):
    def _gap_std(x):
        temp = pd.DataFrame(x)
        return temp.rolling(window1 * window2).apply(lambda m: np.nanstd(m[-1::-window2]), raw=True)

    _gap_std.__name__ = f'df_gap_std_{int(window1)}_{int(window2)}'
    return _gap_std
###########################
# 其他
###########################
def df_quadrant(q1, q2, q3, q4):
    quadrant1 = q1 if q1 == 1 else -1
    quadrant2 = q2 if q2 == 1 else -1
    quadrant3 = q3 if q3 == 1 else -1
    quadrant4 = q4 if q4 == 1 else -1

    def _df_quadrant(x, y):
        _x = pd.DataFrame(x)
        _y = pd.DataFrame(y)

        #
        _x_abs = _x.abs()
        _y_abs = _y.abs()
        #
        _x_sign = np.sign(_x)
        _x_sign[_x_sign == 0] = 1
        _y_sign = np.sign(_y)
        _y_sign[_y_sign == 0] = 1

        #
        output = _x_abs + _y_abs
        #
        output[(_x_sign == 1) & (_y_sign == 1)] = quadrant1 * output
        output[(_x_sign == -1) & (_y_sign == 1)] = quadrant2 * output
        output[(_x_sign == -1) & (_y_sign == -1)] = quadrant3 * output
        output[(_x_sign == 1) & (_y_sign == -1)] = quadrant4 * output

        return output

    _df_quadrant.__name__ = f'df_quadrant_{int(q1)}_{int(q2)}_{int(q3)}_{int(q4)}'
    return _df_quadrant


def df_quadrant2(q1, q2, q3, q4):
    quadrant1 = q1 if q1 == 1 else -1
    quadrant2 = q2 if q2 == 1 else -1
    quadrant3 = q3 if q3 == 1 else -1
    quadrant4 = q4 if q4 == 1 else -1

    def _df_quadrant(x, y):
        _x = pd.DataFrame(x)
        _y = pd.DataFrame(y)

        #
        _x_abs = _x.abs()
        _y_abs = _y.abs()
        #
        _x_sign = np.sign(_x)
        _x_sign[_x_sign == 0] = 1
        _y_sign = np.sign(_y)
        _y_sign[_y_sign == 0] = 1

        #
        output = _x_abs
        #
        output[(_x_sign == 1) & (_y_sign == 1)] = quadrant1 * output
        output[(_x_sign == -1) & (_y_sign == 1)] = quadrant2 * output
        output[(_x_sign == -1) & (_y_sign == -1)] = quadrant3 * output
        output[(_x_sign == 1) & (_y_sign == -1)] = quadrant4 * output

        return output

    _df_quadrant.__name__ = f'df_quadrant2_{int(q1)}_{int(q2)}_{int(q3)}_{int(q4)}'
    return _df_quadrant


def df_quadrant3(q1, q2, q3, q4):
    quadrant1 = q1 if q1 == 1 else 0
    quadrant2 = q2 if q2 == 1 else 0
    quadrant3 = q3 if q3 == 1 else 0
    quadrant4 = q4 if q4 == 1 else 0

    def _df_quadrant(x, y):
        _x = pd.DataFrame(x)
        _y = pd.DataFrame(y)

        #
        _x_sign = np.sign(_x)
        _x_sign[_x_sign == 0] = 1
        _y_sign = np.sign(_y)
        _y_sign[_y_sign == 0] = 1

        #
        output = _x
        #
        output[(_x_sign == 1) & (_y_sign == 1)] = quadrant1 * output
        output[(_x_sign == -1) & (_y_sign == 1)] = quadrant2 * output
        output[(_x_sign == -1) & (_y_sign == -1)] = quadrant3 * output
        output[(_x_sign == 1) & (_y_sign == -1)] = quadrant4 * output

        return output

    _df_quadrant.__name__ = f'df_quadrant3_{int(q1)}_{int(q2)}_{int(q3)}_{int(q4)}'
    return _df_quadrant


def df_clip(threshold):
    def _df_clip(x):
        _x = pd.DataFrame(x)
        _x[_x > threshold] = threshold
        _x[_x < -threshold] = -threshold
        return _x

    _df_clip.__name__ = f'df_clip_{threshold}'
    return _df_clip


def df_clip2(threshold1, threshold2):
    def _df_clip2(x):
        _x = pd.DataFrame(x)
        _x[_x > threshold1] = threshold1
        _x[_x < threshold2] = threshold2
        return _x

    _df_clip2.__name__ = f'df_clip2_{threshold1}_{threshold2}'
    return _df_clip2



