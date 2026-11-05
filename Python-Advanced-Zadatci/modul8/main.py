from abc import ABC, abstractmethod
import streamlit as st


class Person(ABC):
    """Abstract base class representing a person."""

    def __init__(self, name: str, age: int, weight: float, height: float):
        self.name = name.strip()
        self.age = age
        self.weight = weight
        self.height = height

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, value: float):
        if value <= 0:
            raise ValueError("Weight must be strictly greater than zero.")
        self._weight = float(value)

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        if value <= 0:
            raise ValueError("Height must be strictly greater than zero.")
        self._height = float(value)

    @abstractmethod
    def calculate_bmi(self) -> float:
        """Calculate and return Body Mass Index."""
        pass

    @abstractmethod
    def get_bmi_category(self) -> str:
        """Determine and return the BMI category."""
        pass

    def to_dict(self) -> dict:
        """Return formatted record data."""
        bmi = self.calculate_bmi()
        return {
            "Name": self.name,
            "Type": self.__class__.__name__,
            "Age": self.age,
            "Weight (kg)": f"{self.weight:.1f}",
            "Height (m)": f"{self.height:.2f}",
            "BMI": f"{bmi:.2f}",
            "Category": self.get_bmi_category(),
        }


class Adult(Person):
    """Adult BMI calculation and categorization."""

    def calculate_bmi(self) -> float:
        return self.weight / (self.height ** 2)

    def get_bmi_category(self) -> str:
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        if bmi < 25.0:
            return "Normal weight"
        if bmi < 30.0:
            return "Overweight"
        return "Obese"


class Child(Person):
    """Child BMI calculation with age-adjustment factor."""

    def calculate_bmi(self) -> float:
        return (self.weight / (self.height ** 2)) * 1.3

    def get_bmi_category(self) -> str:
        bmi = self.calculate_bmi()
        if bmi < 14.0:
            return "Underweight"
        if bmi < 18.0:
            return "Normal weight"
        if bmi < 24.0:
            return "Overweight"
        return "Obese"


class BMIApp:
    """Streamlit interface and controller for the BMI application."""

    def __init__(self):
        if "people" not in st.session_state:
            st.session_state.people = []

    def add_person(self, person: Person):
        st.session_state.people.append(person)

    def clear_data(self):
        st.session_state.people = []

    def run(self):
        st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")
        st.title("BMI Calculator App")

        # Form batches inputs so the app doesn't re-run on every keystroke
        with st.form("bmi_input_form", clear_on_submit=False):
            name = st.text_input("Name:")
            age = st.number_input("Age:", min_value=1, max_value=120, value=25, step=1)
            weight = st.number_input("Weight (kg):", min_value=1.0, max_value=350.0, value=70.0, step=0.5)
            height = st.number_input("Height (meters):", min_value=0.4, max_value=2.6, value=1.75, step=0.01)

            submitted = st.form_submit_button("Add Person")

        if submitted:
            if not name.strip():
                st.error("Name cannot be empty.")
            else:
                try:
                    if age >= 18:
                        person = Adult(name=name, age=age, weight=weight, height=height)
                    else:
                        person = Child(name=name, age=age, weight=weight, height=height)

                    self.add_person(person)
                    st.success(f"Added {person.name} ({person.__class__.__name__}) successfully!")
                except ValueError as err:
                    st.error(str(err))

        # Results Display
        if st.session_state.people:
            st.markdown("---")
            col1, col2 = st.columns([3, 1])
            with col1:
                st.subheader(f"Recorded People ({len(st.session_state.people)})")
            with col2:
                if st.button("Clear All"):
                    self.clear_data()
                    st.rerun()

            # Display card list using st.write
            for person in st.session_state.people:
                data = person.to_dict()
                st.write(
                    f"**{data['Name']}** ({data['Type']}) — "
                    f"Age: {data['Age']}, Weight: {data['Weight (kg)']} kg, Height: {data['Height (m)']} m | "
                    f"**BMI: {data['BMI']}** (*{data['Category']}*)"
                )


if __name__ == "__main__":
    app = BMIApp()
    app.run()