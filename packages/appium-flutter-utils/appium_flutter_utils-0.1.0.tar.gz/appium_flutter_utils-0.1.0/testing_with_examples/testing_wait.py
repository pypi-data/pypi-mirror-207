from src.appium_flutter_utils.utils import *
from test.driver import *
from appium_flutter_finder import FlutterFinder, FlutterElement
from appium_flutter_report import *


def main():
    driver = webdriver.Remote(appium_server_url, capabilities)
    finder = FlutterFinder()
    UtilsSetup.setup(driver, finder)
    FlutterReportGenerator.setup(driver, "Python Utils", "./output/", capabilities)
    group_testing_wait()
    FlutterReportGenerator.generate_report()


def group_testing_wait():
    test(
        "Initial Setup",
        init,
    )
    test(
        "Wait For Value Key to come",
        testing_wait_for_value_key,

    )
    test(
        "Wait For Value Key to go",
        testing_wait_absence_for_value_key,

    )
    test(
        "Wait For Type to come",
        testing_wait_for_type,
    )
    test(
        "Wait For Type to go",
        testing_wait_absence_for_type,
    )
    test(
        "Wait For Text to come",
        testing_wait_for_text,
    )
    test(
        "Wait For Text to go",
        testing_wait_absence_for_text,
    )
    test(
        "Wait For Semantic to come",
        testing_wait_for_semantic,
    )
    test(
        "Wait For Semantic to go",
        testing_wait_absence_for_semantic,
    )
    test(
        "Wait For Hard Coded to come",
        testing_wait_for_hard_coded,
    )
    test(
        "Wait For Hard Coded to go",
        testing_wait_absence_for_hard_coded,
    )
    test(
        "Wait to come till timeout",
        testing_wait_timeout,
    )
    test(
        "Wait to go till timeout",
        testing_absence_timeout,
    )


def testing_wait_for_value_key(_):
    click("ByValueKey")
    find_element_after_wait = wait("by_value_key", WhatToWait.BY_VALUE_KEY)
    assert find_element_after_wait


def testing_wait_absence_for_value_key(_):
    if finds_some_widgets(UtilsSetup.finder.by_value_key("by_value_key")) is False:
        raise "Cannot find element for which we were waiting"
    click("Reset")
    do_not_find_element_after_wait = wait_for_absence("by_value_key", WhatToWait.BY_VALUE_KEY)
    assert do_not_find_element_after_wait


def testing_wait_for_type(_):
    click("ByType")
    find_element_after_wait = wait("ByTypeWidget")
    assert find_element_after_wait


def testing_wait_absence_for_type(_):
    if finds_some_widgets(UtilsSetup.finder.by_type("ByTypeWidget")) is False:
        raise "Cannot find element for which we were waiting"
    click("Reset")
    do_not_find_element_after_wait = wait_for_absence("ByTypeWidget")
    assert do_not_find_element_after_wait


def testing_wait_for_text(_):
    click("ByText")
    find_element_after_wait = wait("ByTextOutput", WhatToWait.BY_TEXT)
    assert find_element_after_wait


def testing_wait_absence_for_text(_):
    if finds_some_widgets(UtilsSetup.finder.by_text("ByTextOutput")) is False:
        raise "Cannot find element for which we were waiting"
    click("Reset")
    do_not_find_element_after_wait = wait_for_absence("ByTextOutput", WhatToWait.BY_TEXT)
    assert do_not_find_element_after_wait


def testing_wait_for_semantic(_):
    click("BySemanticLabel")
    find_element_after_wait = wait("BySemanticLabelOutput", WhatToWait.BY_SEMANTIC_LABEL)
    assert find_element_after_wait


def testing_wait_absence_for_semantic(_):
    if finds_some_widgets(UtilsSetup.finder.by_semantics_label("BySemanticLabelOutput")) is False:
        raise "Cannot find element for which we were waiting"
    click("Reset")
    do_not_find_element_after_wait = wait_for_absence("BySemanticLabelOutput", WhatToWait.BY_SEMANTIC_LABEL)
    assert do_not_find_element_after_wait


def get_hard_coded() -> str:
    return UtilsSetup.finder.by_descendant(
        UtilsSetup.finder.by_ancestor(
            UtilsSetup.finder.by_semantics_label("ByHardCodedOutput"),
            UtilsSetup.finder.by_type("Row")
        ),
        UtilsSetup.finder.by_type("ByTypeWidget"),
    )


def testing_wait_for_hard_coded(_):
    click("ByHardCoded")
    find_element_after_wait = wait(get_hard_coded(), WhatToWait.HARD_CODED)
    assert find_element_after_wait


def testing_wait_absence_for_hard_coded(_):
    if finds_some_widgets(get_hard_coded()) is False:
        raise "Cannot find element for which we were waiting"
    click("Reset")
    do_not_find_element_after_wait = wait_for_absence(get_hard_coded(), WhatToWait.HARD_CODED)
    assert do_not_find_element_after_wait


def testing_wait_timeout(_):
    click("TimeOut")
    find_element_after_wait = wait("TimeOutOutput", WhatToWait.BY_SEMANTIC_LABEL)
    assert find_element_after_wait is False
    time.sleep(0.5)


def testing_absence_timeout(_):
    if finds_some_widgets(UtilsSetup.finder.by_semantics_label("TimeOutOutput")) is False:
        raise "Cannot find element for which we were waiting"
    click("Reset")
    do_not_find_element_after_wait = wait_for_absence("TimeOutOutput", WhatToWait.BY_SEMANTIC_LABEL)
    assert do_not_find_element_after_wait is False


def init(_):
    FlutterElement(UtilsSetup.driver, UtilsSetup.finder.by_value_key("/WaitTestScreen")).click()
    UtilsSetup.driver.execute_script('flutter:waitFor', UtilsSetup.finder.by_type("WaitTestScreen"), 1500)
    assert finds_some_widgets(UtilsSetup.finder.by_semantics_label("Reset"))


if __name__ == "__main__":
    main()
