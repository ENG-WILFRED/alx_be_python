from book_class import Book
from library_system import Book as BaseBook, EBook, PrintBook, Library
from polymorphism_demo import Rectangle, Circle
from class_static_methods_demo import Calculator

def test_magic_methods():
    print("=== Testing Magic Methods (Book Class) ===")
    my_book = Book("1984", "George Orwell", 1949)
    print(my_book)               # __str__
    print(repr(my_book))         # __repr__
    del my_book                  # __del__ will be triggered
    print()


def test_inheritance_and_composition():
    print("=== Testing Inheritance and Composition (Library System) ===")
    my_library = Library()
    classic = BaseBook("Pride and Prejudice", "Jane Austen")
    digital = EBook("Snow Crash", "Neal Stephenson", 500)
    paper = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    my_library.add_book(classic)
    my_library.add_book(digital)
    my_library.add_book(paper)

    my_library.list_books()
    print()


def test_polymorphism():
    print("=== Testing Polymorphism and Method Overriding ===")
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")
    print()


def test_class_and_static_methods():
    print("=== Testing Class and Static Methods (Calculator) ===")
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")
    print()


def main():
    test_magic_methods()
    test_inheritance_and_composition()
    test_polymorphism()
    test_class_and_static_methods()


if __name__ == "__main__":
    main()
