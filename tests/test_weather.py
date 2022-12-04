from flask import request

import weather
import app
import unittest


class MainTestCase(unittest.TestCase):

    def test_appid_is_set(self):
        assert len(weather.APP_ID) == 32

    def test_parse_error(self):
        assert weather.parse_weather([]) == 'Data error: list indices must be integers or slices, not str'

    def test_convert_temperature(self):
        assert weather.parse_weather({'main': {'temp': '300'}}) == 'The temperature is: 26.9 degree'
        assert weather.parse_weather({'main': {'temp': '273.15'}}) == 'The temperature is: 0.0 degree'

    def test_request(self):
        with app.app.test_client() as c:
            rv = c.get('/weather?city=Moscow')
            assert request.args['city'] == 'Moscow'
            assert rv.status_code == 200

if __name__ == '__main__':
    unittest.main()