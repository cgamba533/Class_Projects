from typing import *
from dataclasses import dataclass
import unittest
import math

calpoly_email_addresses = ["cgamba@calpoly.edu"]

@dataclass(frozen=True)
class GlobeRect:
    def __init__(self, lo_lat, hi_lat, west_long, east_long):
            self.lo_lat = lo_lat
            self.hi_lat = hi_lat
            self.west_long = west_long
            self.east_long = east_long

    """
    Calculate the area of an object of the GlobeRect class. This is done by finding the difference
    between lower and higher latitude coordinates to determine the height and finding the difference
    between Western and Eastern Longitudes to determine the width. Area is then calculated
    and returned by finding the rectangle of the resulting width times height
    """
    def area(self):
        width = abs(self.east_long - self.west_long)
        height = abs(self.hi_lat - self.lo_lat)
        area = width * height
        return area

    def test(self):
        print('hi')

@dataclass(frozen=True)
class Region:
    valid_terrains = ['ocean', 'mountains', 'forest', 'other']
    def __init__(self, rect, name, terrain):
        if terrain in self.valid_terrains:
            self.terrain = terrain
        self.name = name
        self.rect = rect

@dataclass(frozen=True)
class RegionCondition:
    def __init__(self, region, year, pop, ghg_rate):
        self.region = region
        self.year = int(year)
        self.pop = int(pop)
        self.ghg_rate = float(ghg_rate)

    """
    Returns emissions per capita of a given region included as part of a parameter for 
    an object of the RegionCondition class. This is done by returning the regions emissions
    rate divided by its population size.
    """
    def emissions_per_capita(self):
        if self.pop >= 0:
            emissionPerCapita = self.ghg_rate / self.pop
            return emissionPerCapita
        else:
            raise ValueError("Population does not exceed 0")

    """
    Returns emissions per square km of a given region included as part of a parameter for
    an object of the RegionCondition class. This is done by determining the regions area first,
    then dividing that figure by the emissions rate included to then return the emissions rate 
    per square kilometer
    """
    def emissions_per_square_km(self):
        if self.ghg_rate > 0:
            emissionPerSqKm = self.region.rect.area() / self.ghg_rate
            return emissionPerSqKm


PismoBeach_GlobeRect = GlobeRect(-120.713, -120.632, 35.176, 35.136)
PismoBeach_Region = Region(PismoBeach_GlobeRect, 'PismoBeach', 'ocean')
PismoBeach_RegionCondition = RegionCondition(PismoBeach_Region, 2021, 8036, 120801)

SanFransisco_GlobeRect = GlobeRect(-122.446, -122.477, 37.778, 37.729)
SanFransisco_Region = Region(SanFransisco_GlobeRect, 'SanFransisco', 'ocean')
SanFransisco_RegionCondition = RegionCondition(SanFransisco_Region, 2021, 815201, 4100000)

LosAngeles_GlobeRect = GlobeRect(-118.291, -118.508, 34.176, 34.100)
LosAngeles_Region = Region(SanFransisco_GlobeRect, 'LosAngeles', 'ocean')
LosAngeles_RegionCondition = RegionCondition(SanFransisco_Region, 2021, 3849000, 26900000)

CalPoly_GlobeRect = GlobeRect(-120.688, -120.698, 35.258, 35.248)
CalPoly_Region = Region(CalPoly_GlobeRect, 'CalPoly-SLO', 'other')
CalPoly_RegionCondition = RegionCondition(CalPoly_Region, 2021, 47545, 917700)

example_region_conditions = [PismoBeach_RegionCondition, SanFransisco_RegionCondition,
                             LosAngeles_RegionCondition, CalPoly_RegionCondition]

"""
Takes as input a list of objects of the RegionCondition class and returns the object or region with 
the greatest population given region size. This is done by calculating the population per square km 
for each given region and if the current iteration inn the loop exceeds the current list max,
that iteration becomes the new max and its corresponding region name is recorded/updated. Once
the list has been fully processed, the region with the max population per sq km is returned.
"""
def densest(regionList):
    max = 0
    regionName = None
    for i in regionList:
        popPerSqKm = i.pop / i.region.rect.area()
        if popPerSqKm > max:
            max = popPerSqKm
            regionName = i.region.name
    return regionName

"""
The below function takes as input a given object of the RegionCondition class in addition to 
the amount of years that the user would like to estimate the projections out to. The function 
returns estimated population size and emissions rates for the given region object based on 
growth rates which are determined by the terrain type of the region and compounds the result
based on the number of years in the future being projected out to.
"""
def project_condition(Region, numYears):
    if Region.region.terrain == 'ocean':
        new_year = Region.year + numYears
        new_pop = Region.pop * 1.01 ** numYears
        new_ghg = Region.ghg_rate * 1.01 ** numYears
        new_project_condition = RegionCondition(Region.region, new_year, new_pop, new_ghg)
        return new_project_condition
    elif Region.region.terrain == 'mountains':
        new_year = Region.year + numYears
        new_pop = Region.pop * 1.05 ** numYears
        new_ghg = Region.ghg_rate * 1.05 ** numYears
        new_project_condition = RegionCondition(Region.region, new_year, new_pop, new_ghg)
        return new_project_condition
    elif Region.region.terrain == 'forest':
        new_year = Region.year + numYears
        new_pop = Region.pop * 0.999 ** numYears
        new_ghg = Region.ghg_rate * 0.999 ** numYears
        new_project_condition = RegionCondition(Region.region, new_year, new_pop, new_ghg)
        return new_project_condition
    elif Region.region.terrain == 'other':
        new_year = Region.year + numYears
        new_pop = Region.pop * 1.003 ** numYears
        new_ghg = Region.ghg_rate * 1.003 ** numYears
        new_project_condition = RegionCondition(Region.region, new_year, new_pop, new_ghg)
        return new_project_condition
    else:
        return None






# put all test cases in the "Tests" class.
@dataclass(frozen=True)
class Tests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(14,14)

    def test_area(self):
        test = GlobeRect(80, 70, 10, 5)
        result = test.area()
        self.assertEqual(result, 50)

    def test_area_2(self):
        test = GlobeRect(1, 1, 1, 1)
        result = test.area()
        self.assertEqual(result, 0)

    def test_emissions_per_capita(self):
        test = RegionCondition(Region(GlobeRect(1.4, 1, 87.5, 87.8), 'Test', 'mountains'), 2015, 20, 0)
        result = test.emissions_per_capita()
        self.assertEqual(result, 0)

    def test_emissions_per_capita_2(self):
        test = RegionCondition(Region(GlobeRect(1.4, 1, 87.5, 87.8), 'Test', 'mountains'), 2015, 0, 20)
        with self.assertRaises(ZeroDivisionError):
            test.emissions_per_capita()

    def test_emissions_per_sq_km(self):
        test = RegionCondition(Region(GlobeRect(80, 70, 10, 5), 'Test', 'mountains'), 2015, 20, 10)
        result = test.emissions_per_square_km()
        self.assertEqual(result, 5)

    def test_emissions_per_sq_km_2(self):
        test = RegionCondition(Region(GlobeRect(80, 70, 10, 5), 'Test', 'mountains'), 2015, 20, 0)
        result = test.emissions_per_square_km()
        self.assertEqual(result, None)

    def test_densest(self):
        test = example_region_conditions
        result = densest(test)
        expected = 'SanFransisco'
        self.assertEqual(result, expected)

    def test_densest_2(self):
        test = [PismoBeach_RegionCondition]
        result = densest(test)
        expected = 'PismoBeach'
        self.assertEqual(result, expected)

    def test_project_condition(self):
        test = RegionCondition(Region(GlobeRect(80, 70, 10, 5), 'Test', 'mountains'), 2015, 20, 100)
        result = project_condition(test, 5)
        expected = RegionCondition(Region(GlobeRect(80, 70, 10, 5), 'Test', 'mountains'), 2020, 25.5256,
                                   127.62815625000003)
        self.assertEqual(result.pop, expected.pop)
        self.assertEqual(result.ghg_rate, expected.ghg_rate)
        self.assertEqual(result.year, expected.year)
    def test_project_condition_2(self):
        test = RegionCondition(Region(GlobeRect(80, 70, 10, 5), 'Test', 'ocean'), 2015, 20, 100)
        result = project_condition(test, 2)
        expected = RegionCondition(Region(GlobeRect(80, 70, 10, 5), 'Test', 'ocean'), 2017, 20.402, 102.01)
        self.assertEqual(result.pop, expected.pop)
        self.assertEqual(result.ghg_rate, expected.ghg_rate)
        self.assertEqual(result.year, expected.year)

    def test_project_condition_3(self):
        test = RegionCondition(Region(GlobeRect(80, 70, 10, 5), 'Test', 'ocean'), 2015, 20, 100)
        result = project_condition(test, 0)
        expected = RegionCondition(Region(GlobeRect(80, 70, 10, 5), 'Test', 'ocean'), 2015, 20, 100)
        self.assertEqual(result.pop, expected.pop)
        self.assertEqual(result.ghg_rate, expected.ghg_rate)
        self.assertEqual(result.year, expected.year)

if (__name__ == '__main__'):
    unittest.main()
