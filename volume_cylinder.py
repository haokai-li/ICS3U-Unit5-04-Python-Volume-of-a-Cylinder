#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program calculates the volume of a cylinder

import math


def calculate_volume_cylinder(radius, height):
    # This function calculates the volume of a cylinder

    # process
    volume = radius ** 2 * height * math.pi

    return volume


def main():
    # This function just call other functions

    print("This Program calculates the volume of a cylinder.")
    print("Please enter the radius and height.")
    print("")

    # input
    user_radius_string = input("Please enter the radius of a cylinder(cm): ")
    user_height_string = input("Please enter the height of a cylinder(cm): ")
    print("")

    try:
        user_radius_number = float(user_radius_string)
        user_height_number = float(user_height_string)

        # call functions
        calculated_volume_cylinder = calculate_volume_cylinder(
            radius=user_radius_number, height=user_height_number
        )

        # output
        print(
            "The volume of the cylinder is {} cm³.".format(calculated_volume_cylinder)
        )

    except Exception:
        # output
        print("You didn't enter an integer.")

    print("\nDone.")


if __name__ == "__main__":
    main()
