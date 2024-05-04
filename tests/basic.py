from graph_judge import GraphJudge


def basic_test():
    gj = GraphJudge({1, 2, 3, 4})
    gj.add_judge("is_even", lambda x: (x % 2 == 0))
    gj.add_judge("is_one", lambda x: x == 1)

    results = gj.run_chain_and(["is_even", "is_one"])
    evens = results.filter("is_even", True).members()
    one = results.filter("is_one", True).members()
    odd = results.filter("is_even", False).filter("is_one", False).members()

    assert evens == [2, 4]
    assert odd == [3]
    assert one == [1]
