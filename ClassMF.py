class MultipleFunctions:
    def subfields():
        subfields_value = (
            'Machine Learning', 'Neural Networks', 'Vision',
            'Robotics', 'Speech Processing', 'Natural Language Processing'
        )
        print("Sub-fields in AI are:")
        for field in subfields_value:
            print(field)

    def eligible():
        gender = input("Enter your gender (Male/Female): ")
        age = int(input("Enter your age: "))
        if (gender == 'Male' and age >= 21) or (gender == 'Female' and age >= 18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def percentage():
        subject1 = int(input('Enter your Subject1 marks: '))
        subject2 = int(input('Enter your Subject2 marks: '))
        subject3 = int(input('Enter your Subject3 marks: '))
        subject4 = int(input('Enter your Subject4 marks: '))
        subject5 = int(input('Enter your Subject5 marks: '))
        total = subject1 + subject2 + subject3 + subject4 + subject5
        percentage = (total / 500) * 100
        print(f"Total: {total}")
        print(f"Percentage: {percentage:.2f}")
        return percentage

    def area_and_perimeter_of_triangle():
        height = float(input("Enter the height of the triangle: "))
        breadth = float(input("Enter the breadth of the triangle: "))
        area = (height * breadth) / 2
        print("Formula for Area: (height * breadth) / 2")
        print("Area of Triangle:", area)

        side1 = float(input("Enter the first side of the triangle: "))
        side2 = float(input("Enter the second side of the triangle: "))
        side3 = float(input("Enter the third side of the triangle: "))
        perimeter = side1 + side2 + side3
        print("Formula for Perimeter: side1 + side2 + side3")
        print("Perimeter of Triangle:", perimeter)

    def odd_even():
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            text = 'is Even number'
        else:
            text = 'is Odd number'
        result = f"{number} {text}"
        print(result)
        return result
