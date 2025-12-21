1. .* (Dot Star)
. = matches any single character (except newline)

* = matches 0 or more of the preceding character

.* = matches any sequence of characters (including empty string)

Example in Express:

javascript
app.get(/.*fly$/, ...)
// Matches: "/fly", "/butterfly", "/123fly", "/anythingfly"
// The `.*` means "any characters (or none) before 'fly'"
2. + (Plus)
Matches 1 or more of the preceding character

Cannot be zero - must appear at least once

Examples in Express:

javascript
app.get('/ab+cd', ...)
// Matches: "/abcd" (1 b), "/abbcd" (2 b's), "/abbbcd" (3 b's)
// Does NOT match: "/acd" (zero b's - not allowed with +)
3. ? (Question Mark)
Makes the preceding character optional (0 or 1 time)

Means "the previous character may or may not be there"

Examples in Express:

javascript
app.get('/ab?cd', ...)
// Matches: "/acd" (0 b's - optional), "/abcd" (1 b)
// Does NOT match: "/abbcd" (2 b's - ? only allows 0 or 1)