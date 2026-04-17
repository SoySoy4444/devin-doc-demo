# Address API notes

## Purpose
The address API returns the list of saved addresses used by the demo app.

## Endpoint
`GET /api/v1/addresses/`

## Response shape
Each address currently includes:
- `id`
- `street_nr`
- `city`

## Notes for partner teams
- This endpoint is read-only.
- The response is intended for internal demo and partner sandbox usage.
- If the address schema changes, this page should be updated alongside the code.