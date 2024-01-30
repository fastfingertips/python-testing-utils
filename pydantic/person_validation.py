from pydantic import BaseModel, ValidationError

class Person(BaseModel):
    """
    Pydantic Model: Represents the information of a person.

    BaseModel is the fundamental class in Pydantic that allows us
    to create data validation models.
    """
    name: str
    age: int
    email: str

def validate_person_info(data):
    """
    Validates the given data using the Pydantic model.

    :param data: Data to be validated
    :return: Validated data represented by the Pydantic model
    """
    try:
        person = Person(**data)
        return person
    except ValidationError as e:
        print(f"Validation Error: {e}")
        return None

if __name__ == "__main__":
    # Sample data obtained from the user
    user_data = {
        "name": "fastfingertips",
        "age": 20,
        "email": "fastfingertips@example.com"
    }

    # Validate the data
    validated_person = validate_person_info(user_data)

    if validated_person:
        # Print the validated data
        print("Validated Person Information:")
        print(f"Name: {validated_person.name}")
        print(f"Age: {validated_person.age}")
        print(f"Email: {validated_person.email}")
    else:
        print("Invalid input. Please try again.")