from RSquared.strategy import Strategy


if __name__ == "__main__":
    run1 = Strategy()

    print(run1.get_fama_french())
    print(run1._ff_data)
