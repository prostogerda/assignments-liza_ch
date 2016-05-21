def increasing_of_rabbits(reproduct_rabbits: int, month: int) -> int:
    """
    Mating rabbits. Size ofnew generation is sum of sizes of previous
    2 generations and new rabbits (number of reproduct_rabbits or less).
    :param reproduct_rabbits:
    :param month: amount of rabbits by this month
    :return:
    """
    num_previous_month, num_now = 1, 2
    for _ in range(month-1):
        num_now, num_previous_month = num_previous_month + num_now + (reproduct_rabbits
                                                            if num_now > reproduct_rabbits else num_now), num_now
    return num_now

increasing_of_rabbits(5, 3)


def mendel_law(k: int, m: int, n: int) -> float:
    """
    Probability of case, when 2 random organisms from population will give
    the offspring with dominant phenotype (have dominant allele of gene)
    Frequences of organisms in population:
    k- dominant homozygous
    m- heterozygous
    n- recessive homozygous
    :param k:
    :param m:
    :param n:
    :return:
    """
    total = k + m + n
    first_k = k / total
    first_m = 1/2 * m / total * (1/2 * (m-1) / (total - 1) + n / (total - 1))
    first_n = n / total * (k / (total - 1) + 1/2 * m / (total - 1))
    return round(first_k + first_m + first_n, 3)

