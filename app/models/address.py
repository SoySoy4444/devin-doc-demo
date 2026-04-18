from sqlmodel import Field, SQLModel


class AddressBase(SQLModel):
    street_nr: str
    city: str
    country: str = "UK"
    continent: str = "Europe"


class Address(AddressBase, table=True):
    id: int = Field(default=None, primary_key=True)


class AddressCreate(AddressBase):
    pass
