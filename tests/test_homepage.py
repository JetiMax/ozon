# -*- encoding=utf8 -*-
import pytest
from pom.homepage_nav import HomepageNav
from pom.homepage_nav1 import HomepageNav1
from pom.homepage_nav2 import HomepageNav2


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        print(homepage_nav.get_nav_links_text())
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        assert expected_links == actual_links, 'Validation Nav Links Text'


@pytest.mark.usefixtures('setup')
class TestHomepage1:

    def test_nav_links_header(self):
        homepage_nav1 = HomepageNav1(self.driver)
        print(homepage_nav1.get_nav_links_text())
        actual_links = homepage_nav1.get_nav_links_text()
        expected_links = homepage_nav1.NAV_LINK_TEXT
        assert expected_links == actual_links, 'Validation Nav Links Text'


@pytest.mark.usefixtures('setup')
class TestHomepage2:

    def test_nav_links_footer(self):
        homepage_nav = HomepageNav2(self.driver)
        print(homepage_nav.get_nav_links_text())
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        assert expected_links == actual_links, 'Validation Nav Links Text'




