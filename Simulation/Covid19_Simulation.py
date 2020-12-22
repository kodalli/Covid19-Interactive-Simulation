import numpy as np
import multiprocessing


def simulate(initialYoung: tuple = (27199, 0, 1), initialElderly: tuple = (4800, 0, 0),
             Vaccines: int = 0, timeSpanDays: int = 120, maxDataPoints: float = 2e6, runs: int = 1):
    """
    :param initialYoung: (healthy young, healthy young free rider, sick young)
    :param initialElderly: (healthy elderly, healthy elderly free rider, sick elderly)
    :param Vaccines: number of vaccines at time = 0
    :param timeSpanDays: time span in days to run the simulation
    :param maxDataPoints: number of calculations to be done during the time span
    :param runs: number of iterations

    HY  = healthy young
    HE  = healthy elderly
    SY  = sick young 
    SE  = sick elderly 
    I   = immune
    V   = vaccines
    HYF = healthy young free rider "People who refuse to take vaccine"
    HEF = healthy elderly free rider 
    D   = dead 

    Equations:

    HY + SY -> 2SY          k0= 1.76e-5 day^-1      r0 = k[0]*HY*SY
    HY + SE -> SY + SE                              r1 = k[0]*HY*SE
    HYF + SY -> 2SY                                 r2 = k[0]*HYF*SY
    HYF + SE -> SY + SE                             r3 = k[0]*HYF*SE

    HE + SY -> SY + SE      k1= 0.88e-5 day^-1      r4 = k[1]*HE*SY
    HE + SE -> 2SE                                  r5 = k[1]*HE*SE
    HEF + SY -> SY + SE                             r6 = k[1]*HEF*SY
    HEF + SE -> 2SE                                 r7 = k[1]*HEF*SE

    SY -> D                 k2= 0.010 day^-1        r8 = k[2]*SY
    SE -> D                 k3= 0.030 day^-1        r9 = k[3]*SE

    SY -> I                 k4= 0.100 day^-1        r10= k[4]*SY
    SE -> I                                         r11= k[4]*SE

    HY + V -> I             k5= 3.52e-6 day^-1      r12= k[5]*HY*V
    HE + V -> I                                     r13= k[5]*HE*V
    """
    HY0, HYF0, SY0 = initialYoung
    HE0, HEF0, SE0 = initialElderly
    D0, V0, I0 = 0, Vaccines, 0
    n0 = (HY0, HYF0, HE0, HEF0, SY0, SE0, D0, V0, I0)  # inital conditions
    k = [1.76e-5, 0.88e-5, 0.010, 0.030, 0.100,
         3.52e-6]  # day^-1 rate constants

    args = [(n0, k, timeSpanDays, maxDataPoints) for _ in range(runs)]
    pool = multiprocessing.Pool()
    gil_deaths = pool.map(gillespie, args)
    print(gil_deaths)


def gillespie(*args):
    """ 
        Gillespie algorithm allows for a discrete stochastic model
        of the disease. The reactions are converted to probabilites
        and if the reaction occurs, each element is changed relative
        to the reaction and avoiding fractional changes.

        For example, lets observe the reaction HY + SY -> 2SY. If the
        probability of the reaction is calculated to be 0.5, this
        means there is a 50% chance for this reaction to occur. 
        Using a numpy uniform distribution we can simulate the event
        probability akin to flipping a coin. If the random number 
        is less than the cumulative probability of the event occuring
        then the reaction will occur. In this case 1 
        healthy young person + a sick young person will become 
        2 sick young people. If the reaction doesn't occur then
        there are no changes to the population's identites. The healthy
        person will stay healthy and the sick person will stay sick.
        When a healthy person becomes sick, they are subtracted from
        the population of healthy people and added to the population
        of sick people. 

        This model assumes each group has a 1st degree affect on the
        rate of reaction.

        n = [HY, HE, HYF, HEF, SY, SE, D, V, I]
        k = [k0, k1, k2, k3, k4, k5]
    """
    args = args[0]
    print(args)
    n, k, tSpan, nMax = args[0], args[1], args[2], args[3]
    time = np.zeros(int(nMax))
    t = 0
    result = np.zeros((int(nMax), 9), dtype=np.uint64)
    nV0 = n[7]
    last_val = 0
    vacc = True
    for index in range(len(time)):
        if(vacc and t >= 30):
            n[7] += nV0/2  # add new vaccines
            vacc = False

        r = get_r(n, k)  # rxn proportional probabilities
        rtot = np.sum(r)

        if(rtot == 0 or t >= tSpan):  # stop condition
            last_val = index
            break

        w = np.random.uniform()
        tau = -np.log(w)/rtot  # time step
        result[index] = n
        time[index] = t
        t += tau
        rprob = np.array([i/rtot for i in r])  # rxn probabilities
        csp = np.cumsum(rprob)
        q = np.random.uniform()

        for i, item in enumerate(csp):
            if(q < item):  # if the rand num is less than cumulative prob then the rxn occurs
                rxn_num = i
                n = nvsum(n, rxn_num)
                break

    # stores only results till recorded time index
    res = result.T[:, :last_val]
    print(res.shape)
    return res[6, -1]  # deaths


def nvsum(n, rxn_num):
    """
        Helper function, sums the reaction with the current number of items.

        rxn_num = int representing which reaction to apply to the population

        n = [HY, HE, HYF, HEF, SY, SE, D, V, I], these are all the number 
        of each element, HY is number of healthy young people, V is number
        of vaccines etc.
    """
    # n = [HY, HE, HYF, HEF, SY, SE, D, V, I]
    v = np.array((
        [-1, 0, 0, 0, 1, 0, 0, 0, 0],
        [-1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, -1, 0, 1, 0, 0, 0, 0],
        [0, 0, -1, 0, 1, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 1, 0, 0, 0],
        [0, -1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, -1, 0, 1, 0, 0, 0],
        [0, 0, 0, -1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, -1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, -1, 1, 0, 0],
        [0, 0, 0, 0, -1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, -1, 0, 0, 1],
        [-1, 0, 0, 0, 0, 0, 0, -1, 1],
        [0, -1, 0, 0, 0, 0, 0, -1, 1]
    ))
    # if reaction index 2 occurs then subtract 1 healthy young person
    # and add 1 sick young person to the total population represented by n
    n = np.add(n, v[rxn_num])
    return n


def get_r(n, k):
    """
        Helper function for the Gillespie algorithm.
        Gets the relative reaction probabilites.

        n = count for each element ex: V is number of vaccines
        k = all the reaction rate constants in days^-1
    """
    HY, HE, HYF, HEF, SY, SE, D, V, I = n
    r = np.array([
        k[0]*HY*SY,
        k[0]*HY*SE,
        k[0]*HYF*SY,
        k[0]*HYF*SE,
        k[1]*HE*SY,
        k[1]*HE*SE,
        k[1]*HEF*SY,
        k[1]*HEF*SE,
        k[2]*SY,
        k[3]*SE,
        k[4]*SY,
        k[4]*SE,
        k[5]*HY*V,
        k[5]*HE*V
    ])
    return r


if __name__ == "__main__":
    simulate(initialYoung=(27199, 1000, 500), initialElderly=(4800, 1000, 350), Vaccines=1000, runs=64)
