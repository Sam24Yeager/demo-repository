from time import sleep
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


#launching the browser and opening the travel website
from test_automation.base.basepage import BaseDriver
from test_automation.pages.launchPage import LaunchPage
from test_automation.pages.searchResultsPage import SearchResults
from time import sleep


@pytest.mark.usefixtures('setup')
class Test_script:
    def test_function(self):

        #launch browser and launching the website


        #provide depart from location
        lp=LaunchPage(self.driver)
        lp.departFrom('new delhi')
        sleep(2)


        #provide going to location
        lp.goingTO('new')
        sleep(2)



         #to select the departure date
         lp.departureDate('24/01/2023')
         sleep(2)



         #click on flight search button
         lp.searchButton()
         sleep(2)


        self.driver.set_page_load_timeout(100)
        self.driver.get('https://flight.yatra.com/air-search-ui/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=BOM&destinationCountry=IN&flight_depart_date=10%2F01%2F2023&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home&unqvaldesktop=1012116628059')
        # ele=self.driver.find_element(By.XPATH,"(//p[@class='font-lightgrey bold'])[2]")
        # self.wait.until(EC.visibility_of(ele))


        #to handle dynamic scroll button
        lp.scrollButton()

        sleep(2)

        #select the filter one stop
        sp=SearchResults(self.driver)
        sp.filter()

        all_stops = self.wait.until( EC.presence_of_all_elements_located((By.XPATH, "//span[@class='dotted-borderbtm']")))
        print(len(all_stops))


        #verify that filtered results having 1 stop
        for i in all_stops:
            assert i.text == "1 Stop"
            print('assert pass')
        sleep(4)
