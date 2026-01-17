# Code Review Notes

## Summary
All three AI-generated tasks contained critical mathematical errors in calculating averages. Two tasks (Task 1 and Task 3) shared the identical bug: dividing by total input length instead of the count of valid (non-filtered) elements.

## Pattern Analysis
**Systematic Issue**: The AI model appears to have a conceptual misunderstanding of calculating averages when filtering data. Both tasks that filter out invalid data (cancelled orders, None values) failed to adjust the denominator accordingly.

- **Task 1 & 3**: Identical off-by-X error in division denominator
- **Task 2**: Different class of error—overly permissive validation where checking for presence of `@` alone is insufficient

## Design Decisions in Corrections

1. **Error Handling Strategy**: Chose explicit `ValueError` with descriptive messages rather than silent failures or uncaught exceptions. This provides:
   - Clear debugging information
   - Fail-fast behavior (safer than returning misleading results)
   - Explicit contract that consumers must handle the error case

2. **Task 2 Email Validation**: 
   - Implemented minimal format validation (exactly one `@`, non-empty parts)
   - Did NOT implement full RFC 5322 compliance (would be overengineering for this scope)
   - Gracefully skips non-string types (comment documents this)
   - Trade-off: Accepts minimal valid formats like `"a@b"` but rejects obvious malformations

3. **Task 3 Type Conversion**: 
   - Preserved implicit float() conversion (accepts mixed numeric types)
   - Non-numeric strings will raise TypeError (this is acceptable—invalid data should fail explicitly)
   - Alternative considered: Pre-validate all values, but decided the current approach is simpler and equally correct

## Testing Notes
All corrected implementations were validated against:
- Normal cases (expected inputs)
- Edge cases (empty, all-filtered, boundary values)
- Error cases (invalid data, zero valid entries)

All tests passed. Implementations are production-ready.
