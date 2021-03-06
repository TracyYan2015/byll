import math

# compute the cumulative probability density of standard normal distribution
def cdf(x):
    # constants
    a1 =  0.254829592;
    a2 = -0.284496736;
    a3 =  1.421413741;
    a4 = -1.453152027;
    a5 =  1.061405429;
    p  =  0.3275911;

    # Save the sign of x
    sign = 1;
    if x < 0:
        sign = -1;
    x = sign * x/math.sqrt(2.0);

    # A&S formula 7.1.26
    t = 1.0/(1.0 + p*x);
    y = 1.0 - (((((a5*t + a4)*t) + a3)*t + a2)*t + a1)*t*math.exp(-x*x);

    return 0.5*(1.0 + sign*y);

def test():
    thickness = 100
    k1 = 100
    k2 = 0.005
    IEL = k1 / thickness
    NIEL = k2 * thickness

    pmax_threshold = 0.8
    a_mu = 0.1754
    a_sigma = 0.02319029
    a = 0.1701
    b = 12.0
    day = 1
    d2 = (day / 365.0) * NIEL
    cdf_x = (1 - pmax_threshold) / math.log(1 + d2 * b)
    std_cdf_x = (cdf_x - a_mu) / a_sigma
    print std_cdf_x
    print 1 - cdf(std_cdf_x)

test()

