from src.appium_flutter_utils.utils import *
from test.driver import *
from appium_flutter_finder import FlutterFinder
from appium_flutter_report import *
from testing_click import group_testing_click
from testing_double_click import group_testing_double_click
from testing_long_click import group_testing_long_click
from testing_wait import group_testing_wait
from testing_enter_text import group_testing_enter_text
from testing_scroll import group_testing_scroll


def main():
    driver = webdriver.Remote(appium_server_url, capabilities)
    finder = FlutterFinder()
    UtilsSetup.setup(driver, finder)
    FlutterReportGenerator.setup(driver, "Python Utils", "./output/", capabilities)
    group(
        "Testing Click",
        group_testing_click,
    )
    __go_back()
    group(
        "Testing Double Click",
        group_testing_double_click,
    )
    __go_back()
    group(
        "Testing Long Click",
        group_testing_long_click,
    )
    __go_back()
    group(
        "Testing Wait",
        group_testing_wait,
    )
    __go_back()
    group(
        "Testing Enter Text",
        group_testing_enter_text,
    )
    __go_back()
    group(
        "Testing Scroll",
        group_testing_scroll,
    )
    FlutterReportGenerator.generate_report()


def __go_back():
    UtilsSetup.driver.switch_to.context("NATIVE_APP")
    UtilsSetup.driver.back()
    UtilsSetup.driver.switch_to.context("FLUTTER")


if __name__ == "__main__":
    main()
