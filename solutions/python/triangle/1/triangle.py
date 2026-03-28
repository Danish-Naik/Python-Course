def is_valid(sides):
    a, b, c = sides
    return (
        a > 0 and b > 0 and c > 0 and
        a + b >= c and
        b + c >= a and
        a + c >= b
    )


def equilateral(sides):
    """Return True if triangle is equilateral."""
    if not is_valid(sides):
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    """Return True if triangle is isosceles."""
    if not is_valid(sides):
        return False
    return (
        sides[0] == sides[1] or
        sides[1] == sides[2] or
        sides[0] == sides[2]
    )


def scalene(sides):
    """Return True if triangle is scalene."""
    if not is_valid(sides):
        return False
    return (
        sides[0] != sides[1] and
        sides[1] != sides[2] and
        sides[0] != sides[2]
    )