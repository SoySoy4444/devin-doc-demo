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
- `country` (defaults to `"UK"` when not supplied)
- `continent` (defaults to `"Europe"` when not supplied)

## Notes for partner teams
- This endpoint is read-only.
- The response is intended for internal demo and partner sandbox usage.
- Payloads are additive: existing consumers that ignore unknown fields will keep working as `country` and `continent` are added to the response.
- If the address schema changes, this page should be updated alongside the code.

## Migration notes
- `country` (default `"UK"`) and `continent` (default `"Europe"`) are added to `AddressBase`, so existing `AddressCreate` callers do not need to change.
- Existing rows will serialize with the default values on read; no Alembic migration is included in the source PR, so no column-level backfill is required for the SQLite demo.