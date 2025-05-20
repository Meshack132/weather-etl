from etl.transform import clean_weather_data

def test_clean_weather_data():
    mock_input = {
        "name": "TestCity",
        "main": {"temp": 20.5, "humidity": 75}
    }
    result = clean_weather_data(mock_input)
    assert result["city"] == "TestCity"
    assert result["temp"] == 20.5
    assert result["humidity"] == 75
