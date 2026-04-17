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
- `country` (defaults to `"UK"` when an address is created without one)
- `continent` (defaults to `"Europe"` when an address is created without one)

## Notes for partner teams
- This endpoint is read-only.
- The response is intended for internal demo and partner sandbox usage.
- If the address schema changes, this page should be updated alongside the code.
- Consumers should treat the address payload as additive: new string fields
  (such as `country` and `continent`) may be introduced over time and should
  not cause strict parsers to fail.

## Migration notes
- `country` and `continent` were added to the address model in
  [PR #6](https://github.com/SoySoy4444/devin-doc-demo/pull/6).
- Both fields have server-side defaults (`country="UK"`, `continent="Europe"`),
  so existing `POST` clients that omit them continue to work without changes.
- `GET` responses now include `country` and `continent` on every address.
  Strict client schemas that reject unknown fields will need to be updated to
  accept them.
- Reviewer note: the source PR updates the SQLModel definition only; no
  Alembic migration was added in that PR. If a migration is expected to ship
  alongside the model change, this section should be expanded once the
  migration lands.
