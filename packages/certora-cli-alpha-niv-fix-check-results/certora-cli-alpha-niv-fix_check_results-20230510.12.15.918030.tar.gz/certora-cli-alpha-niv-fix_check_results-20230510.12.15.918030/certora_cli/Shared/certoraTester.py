from typing import Any, Dict, List, Optional, Tuple, Set
from tabulate import tabulate

errors = ""
warnings = ""
table = []  # type: List[List[str]]
violations_headers = ["Test name", "Rule", "Function", "Result", "Expected"]


def addError(errors: str, testName: str, rule: str, ruleResult: str, expectedResult: str = "",
             funcName: str = "") -> str:
    errors += "Violation in " + testName + ": " + rule
    if funcName != "":
        errors += ", " + funcName
    errors += " result is " + ruleResult + "."
    if expectedResult != "":
        errors += "Should be " + expectedResult
    errors += "\n"
    return errors


def print_table(headers: List[str]) -> None:
    print(tabulate(table, headers, tablefmt="psql"))


def findExpected(funcName: str, resultsList: Dict[str, List[str]]) -> str:
    expectedResult = "\033[33mundefined\033[0m"
    for result in resultsList.keys():
        if funcName in resultsList[result]:
            expectedResult = result
            break
    return expectedResult


def appendViolation(table: List[List[str]], testName: str, actualResult: str, expectedResult: str,
                    ruleName: str = "", funcName: str = "") -> None:
    tableRow = []
    tableRow.append(testName)
    tableRow.append(ruleName)
    tableRow.append(funcName)
    tableRow.append(actualResult)
    tableRow.append(expectedResult)

    table.append(tableRow)

def compare_flat_to_nested_rule(flat_status: str, nested: Dict[str, List[str]]) -> bool:
    """Compares the status of a flat rule with the status of a nested rule.

    Args:
        flat_status (str): The status of the flat rule.
        nested (Dict[str, List[str]]): The status of the nested rule, organized as a dictionary where the keys are the
            possible status values and the values are lists of functions that correspond to that status.

    Returns:
        bool: True in 2 cases: 
            1. if the flat rule succeeded and all non-success statuses in the nested rule have no corresponding functions;
            2. if the flat rule is not succeeded (for example timeout) at least one function in the nested is corresponding to that status
            False otherwise.
    """
    if flat_status == 'SUCCESS': 
        for status, func_list in nested.items():
            if status != 'SUCCESS' and len(func_list) > 0:
                return False
        return True
    else:
        return len(nested[flat_status]) > 0


# compare jar results with expected
# @param rulesResults is a dictionary that includes all the rule names and their results from the jar output
# @param expectedRulesResults is a dictionary that includes all the rule names and their results from tester file
# @param assertMessages is a dictionary that includes all the rule names and their assertion messages
#        from the jar output
# @param expectedAssertionMessages is a dictionary that includes all the rule names and their assertion messages
#        from tester file
# @param test is a boolean indicator of current test (test==false <=> at least one error occured)
def compareResultsWithExpected(
        testName: str,
        rulesResults: Dict[str, Any],
        expectedRulesResults: Dict[str, Any],
        assertMessages: Dict[str, Any],
        expectedAssertionMessages: Optional[Dict[str, Any]],
        test: bool = True
) -> bool:
    global errors
    global warnings

    violations: Set[Tuple] = set()

    if rulesResults != expectedRulesResults:
        # compare results in expected 
        compare_results(rulesResults, expectedRulesResults, violations, testName)
        # compare expected in results
        compare_results(expectedRulesResults, rulesResults, violations, testName)
    
    # if assertMessages field is defined (in tester)
    if expectedAssertionMessages:
        test = compare_assert_messages(testName, expectedAssertionMessages, assertMessages)
    
    for t in violations:
        appendViolation(*t)

    test = len(violations) == 0

    return test



def compare_results(results: Dict[str,Any], expected: Dict[str,Any], violations: Set[Tuple], testName: str):
    for rule, ruleResult in results.items():
            if rule in expected.keys():
                expectedRuleResult = expected[rule]
                if isinstance(ruleResult, str):
                    if isinstance(expectedRuleResult, str): # and the rule is flat in the expected as well
                        if ruleResult != expectedRuleResult:
                            # errors = addError(errors, testName, rule, ruleResult, expectedRuleResult)
                            violations.add((table, testName, ruleResult, expectedRuleResult, rule, ""))
                    else: # the rule is nested in the expected

                        if not compare_flat_to_nested_rule(ruleResult, expectedRuleResult):
                            # errors = addError(errors, testName, rule, ruleResult, expectedRuleResult)
                            violations.add((table, testName, ruleResult, expectedRuleResult, rule, ""))
                
                else:  # nested rule ( ruleName: {result1: [funcionts list], result2: [funcionts list] ... } )
                    if isinstance(expectedRuleResult, str): # but the rule is not nested in the expected
                        if not compare_flat_to_nested_rule(expectedRuleResult, ruleResult):
                            # errors = addError(errors, testName, rule, ruleResult, expectedRuleResult)
                            violations.add((table, testName, ruleResult, expectedRuleResult, rule, ""))

                    else:  # both rules are nested
                        for result, funcList in ruleResult.items():
                            funcList.sort()
                            expectedRuleResult[result].sort()

                            # compare functions lists (current results with expected)
                            if funcList != expectedRuleResult[result]:
                                for funcName in funcList:
                                    # if function appears in current results but does not appear in the expected ones
                                    if funcName not in expectedRuleResult[result]:
                                        # errors = addError(errors, testName, rule, result, "", funcName)
                                        # found results for an unexpected rule
                                        expectedResult = findExpected(funcName, expectedRuleResult)
                                        violations.add(((table, testName, result, expectedResult, rule, funcName)))
            else:
                result = (ruleResult
                          if isinstance(ruleResult, str)
                          else "Object{" + ", ".join(ruleResult.keys()) + "}")
                violations.add((table, testName, result, "\033[33mundefined\033[0m", rule, ""))
                # errors += testName + ", " + rule + " is not listed in 'rules'. Expected rules: " + \
                # ','.join(expectedRulesResults.keys()) + "\n"


def compare_assert_messages(testName: str, expectedAssertionMessages: Dict[str,Any], assertMessages: Dict[str,Any]) -> bool:
        test = True
        for rule in expectedAssertionMessages.keys():
            if rule not in assertMessages:  # current rule is missing from 'assertMessages' section in current results
                test = False
                errors += testName + ", rule \"" + rule + \
                    "\" does not appear in the output. Please, remove unnecessary rules.\n"
            elif expectedAssertionMessages[rule] != assertMessages[rule]:
                # assertion messages are different from each other
                test = False
                errors += testName + ", rule \"" + rule + "\": wrong assertion message. Got: \"" + \
                    assertMessages[rule] + "\". Expected: \"" + expectedAssertionMessages[rule] + "\".\n"
        return test


def get_errors() -> str:
    return errors


def has_violations() -> bool:
    if table:
        return True
    else:
        return False


def get_violations() -> None:
    if table:
        print("Found violations:")
        print_table(violations_headers)
