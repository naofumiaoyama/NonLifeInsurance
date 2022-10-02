Contract ER

```puml
@startuml
entity "CarMaster" {
    + id: ULID [PK]
    ==
     # type_id:  [FK(TypeMaster,id)]
    name: varchar(256)
    vehicle_model: varchar(20)
}

entity "TypeMaster" {
    + id: ULID [PK]
    ==
    type_group: varchar(10)
    type_name: varchar(10)
}

entity "InsuranceMaster" {
    + id: ULID [PK]
    ==
    product_code: varchar(20)
    name: varchar(256)
    # insurance_type_id:  [FK(TypeMaster,id)]
}

entity "OrganizationMaster" {
    + id: ULID [PK]
    ==
    name: varchar(256)
    # type_id: [FK(TypeMaster,id)]
}

entity "Contracts" {
    + id: ULID [PK]
    ==
    # insurance_id: [FK(Insurance,id)]
    policy_number: varchar(20)
    amount: decimal
    rate: decimal
    premium: decimal
}

entity "Insurances" {
    + id: ULID [PK]
    ==
    # insurance_master_id: [FK(InsuranceMaster,id)]
    # person_id: [FK(Persons,id)]
    # building_id: [FK(Buildings,id)]
    # organization_id: [FK(,id)]
    # car_id: [FK(Cars,id)]
}

entity "Persons" {
    + id: ULID [PK]
    ==
    first_name: varchar(20)
    middle_name: varchar(20)
    last_name: varchar(20)
    # person_type_id:  [FK(TypeMaster,id)]

}

entity "Addresses" {
    + id: ULID [PK]
    ==
    # person_id: ULID [FK(Persons,id)]
    # organization_id: ULID [FK(OrganizationMaster,id)]
    # building_id: ULID [FK(Buildings,id)]
    zipcode: varchar(20)
    prefecture_code: varchar(10)
    city_ward_name: varchar(50)
    street: varchar(50)
    building_name: varchar(50)
    room_number: varchar(50)
}

entity "Organizations" {
    + id: ULID [PK]
    ==
    name: varchar(256)
}

entity "Cars" {
    + id: ULID [PK]
    ==
    # person_id: ULID [FK(Persons,id)]
    # car_master_id: ULID [FK(CarMaster,id)]
}

entity "Buildings" {
    + id: ULID [PK]
    ==
    # person_id: ULID [FK(Persons,id)]
    name: varchar(256)
}


@enduml
```
