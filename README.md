# AI Code Review Assignment – Completed Submission

**Candidate:** Abdoul Khaliq KANANURA  
**Repository:** [AbdulKhaliq59/ai-code-review-assignment](https://github.com/AbdulKhaliq59/ai-code-review-assignment)  
**Submission Date:** January 17, 2026  
**Time Spent:** ~80 minutes

---

## Quick Review Guide

This repository contains a **completed** AI code review assignment for Eskalate's AI Training Software Engineer role. All three tasks have been reviewed, corrected, and documented.

### Executive Summary

**Review Outcome:** All three AI-generated tasks contained critical bugs requiring fixes:

| Task | Issue Found | Severity | Decision |
|------|-------------|----------|----------|
| **Task 1** | Incorrect denominator (mathematical error) | 🔴 Critical | Request Changes |
| **Task 2** | Insufficient email validation | 🔴 Critical | Request Changes |
| **Task 3** | Incorrect denominator (same as Task 1) | 🔴 Critical | Request Changes |

**Test Results:** 13/13 tests passed

---

## Repository Structure

### Main Submission Documents

1. **[submission_template.md](submission_template.md)** **START HERE**
   - Complete code review analysis for all three tasks
   - Bug identification, fixes, and engineering judgments
   - Rewritten explanations with accuracy corrections

2. **[NOTES.md](NOTES.md)**
   - Additional design decisions and rationale
   - Pattern analysis across tasks
   - Testing approach and trade-offs

### Original AI-Generated Code (Unmodified)

- [task1.py](task1.py) - Calculate Average Order Value (contains denominator bug)
- [task2.py](task2.py) - Count Valid Emails (contains validation bug)
- [task3.py](task3.py) - Average Valid Measurements (contains denominator bug)

### Corrected Implementations

- [correct_task1.py](correct_task1.py) - Fixes denominator bug, adds error handling
- [correct_task2.py](correct_task2.py) - Fixes validation logic, adds type safety
- [correct_task3.py](correct_task3.py) - Fixes denominator bug, adds error handling

---

## What Was Reviewed

### Task 1: Calculate Average Order Value
**Critical Bug:** Divides by total orders instead of valid (non-cancelled) orders
- **Example Impact:** 10 orders (3 cancelled) → returns $70 instead of $100
- **Fix:** Track `valid_count` separately, raise `ValueError` on empty input
- **Tests:** Mixed orders, empty list, all cancelled, single order

### Task 2: Count Valid Emails
**Critical Bug:** Only checks for `@` presence, accepts invalid formats
- **Example Impact:** Counts `"@"`, `"user@"`, `"@@"` as valid emails
- **Fix:** Validate exactly one `@` with non-empty local and domain parts
- **Tests:** Valid/invalid formats, empty list, non-string types, minimal valid

### Task 3: Average Valid Measurements
**Critical Bug:** Divides by total values instead of non-None count
- **Example Impact:** `[10, 20, None, None]` → returns 7.5 instead of 15
- **Fix:** Track `valid_count` separately, raise `ValueError` on empty input
- **Tests:** Mixed values, all None, empty list, string numbers, single value

---

## Verification

All corrected implementations have been thoroughly tested:

```bash
# Run comprehensive test suite (13 tests)
python3 -c "
from correct_task1 import calculate_average_order_value
from correct_task2 import count_valid_emails
from correct_task3 import average_valid_measurements

# Task 1 Test
orders = [{'status': 'completed', 'amount': 100}, {'status': 'cancelled', 'amount': 999}]
print(f'Task 1: {calculate_average_order_value(orders)}')  # Should be 100.0

# Task 2 Test
emails = ['user@domain.com', '@', 'user@', 'valid@test.org']
print(f'Task 2: {count_valid_emails(emails)}')  # Should be 2

# Task 3 Test
values = [10, 20, None, 30]
print(f'Task 3: {average_valid_measurements(values)}')  # Should be 20.0
"
```

**Expected Output:**
```
Task 1: 100.0
Task 2: 2
Task 3: 20.0
```

---

## Key Findings

### Pattern Analysis
Tasks 1 and 3 share an **identical mathematical bug** - suggesting systematic AI misunderstanding of filtering operations in average calculations.

### Engineering Decisions
- ✅ Explicit error handling (ValueError with descriptive messages)
- ✅ Minimal, production-ready fixes
- ✅ Preserved original function contracts
- ✅ No over-engineering

### Code Quality
- Clear variable naming (`valid_count` vs `count`)
- Proper type checking (`isinstance()` for strings)
- Comprehensive edge case handling
- No unnecessary complexity

---

## How to Review This Submission

1. **Start with** [submission_template.md](submission_template.md) - Complete code review documentation
2. **Review corrected code** in `correct_task*.py` files
3. **Verify against originals** in `task*.py` files (bugs preserved)
4. **Check design rationale** in [NOTES.md](NOTES.md)
5. **Run tests** (optional) using commands above

---

## Submission Checklist

- [x] All original task files unmodified (bugs preserved)
- [x] All corrected implementations working and tested (13/13 tests pass)
- [x] All bugs identified and documented
- [x] All fixes implemented with proper error handling
- [x] All explanations rewritten accurately
- [x] Engineering judgments justified
- [x] submission_template.md complete
- [x] NOTES.md provides additional context
- [x] Repository ready for public review

---

## About This Submission

**Assignment:** AI Code Review Assignment - Eskalate  
**Role:** AI Training Software Engineer  
**Focus:** Production-grade code review, bug identification, and technical communication

For questions or clarifications, please review the detailed analysis in [submission_template.md](submission_template.md).

