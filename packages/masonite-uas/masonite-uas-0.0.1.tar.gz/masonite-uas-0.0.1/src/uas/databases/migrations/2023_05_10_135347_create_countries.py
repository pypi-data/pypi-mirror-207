"""CreateCountries Migration."""

from masoniteorm.migrations import Migration

import json

from masoniteorm.query import QueryBuilder

class CreateCountries(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("countries") as table:
            table.increments("id")
            table.string("name", 128).unique()
            table.string("capital", 128) .nullable()
            table.timestamps()

        # populate countries table
        builder = QueryBuilder().table("countries")
        builder.bulk_create(self.countries())


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("countries")


    def countries(self): 
        return [
            {
                "name": "Afghanistan",
                "capital": "Kabul"
            },
            {
                "name": "Albania",
                "capital": "Tirana"
            },
            {
                "name": "Algeria",
                "capital": "Alger"
            },
            {
                "name": "American Samoa",
                "capital": "Fagatogo"
            },
            {
                "name": "Andorra",
                "capital": "Andorra la Vella"
            },
            {
                "name": "Angola",
                "capital": "Luanda"
            },
            {
                "name": "Anguilla",
                "capital": "The Valley"
            },
            {
                "name": "Antarctica",
                "capital": None
            },
            {
                "name": "Antigua and Barbuda",
                "capital": "Saint John's"
            },
            {
                "name": "Argentina",
                "capital": "Buenos Aires"
            },
            {
                "name": "Armenia",
                "capital": "Yerevan"
            },
            {
                "name": "Aruba",
                "capital": "Oranjestad"
            },
            {
                "name": "Australia",
                "capital": "Canberra"
            },
            {
                "name": "Austria",
                "capital": "Wien"
            },
            {
                "name": "Azerbaijan",
                "capital": "Baku"
            },
            {
                "name": "Bahamas",
                "capital": "Nassau"
            },
            {
                "name": "Bahrain",
                "capital": "al-Manama"
            },
            {
                "name": "Bangladesh",
                "capital": "Dhaka"
            },
            {
                "name": "Barbados",
                "capital": "Bridgetown"
            },
            {
                "name": "Belarus",
                "capital": "Minsk"
            },
            {
                "name": "Belgium",
                "capital": "Bruxelles [Brussel]"
            },
            {
                "name": "Belize",
                "capital": "Belmopan"
            },
            {
                "name": "Benin",
                "capital": "Porto-Novo"
            },
            {
                "name": "Bermuda",
                "capital": "Hamilton"
            },
            {
                "name": "Bhutan",
                "capital": "Thimphu"
            },
            {
                "name": "Bolivia",
                "capital": "La Paz"
            },
            {
                "name": "Bosnia and Herzegovina",
                "capital": "Sarajevo"
            },
            {
                "name": "Botswana",
                "capital": "Gaborone"
            },
            {
                "name": "Bouvet Island",
                "capital": None
            },
            {
                "name": "Brazil",
                "capital": "Brasília"
            },
            {
                "name": "British Indian Ocean Territory",
                "capital": None
            },
            {
                "name": "Brunei",
                "capital": "Bandar Seri Begawan"
            },
            {
                "name": "Bulgaria",
                "capital": "Sofia"
            },
            {
                "name": "Burkina Faso",
                "capital": "Ouagadougou"
            },
            {
                "name": "Burundi",
                "capital": "Bujumbura"
            },
            {
                "name": "Cambodia",
                "capital": "Phnom Penh"
            },
            {
                "name": "Cameroon",
                "capital": "Yaounde"
            },
            {
                "name": "Canada",
                "capital": "Ottawa"
            },
            {
                "name": "Cape Verde",
                "capital": "Praia"
            },
            {
                "name": "Cayman Islands",
                "capital": "George Town"
            },
            {
                "name": "Central African Republic",
                "capital": "Bangui"
            },
            {
                "name": "Chad",
                "capital": "N'Djamena"
            },
            {
                "name": "Chile",
                "capital": "Santiago de Chile"
            },
            {
                "name": "China",
                "capital": "Peking"
            },
            {
                "name": "Christmas Island",
                "capital": "Flying Fish Cove"
            },
            {
                "name": "Cocos (Keeling) Islands",
                "capital": "West Island"
            },
            {
                "name": "Colombia",
                "capital": "Santaf"
            },
            {
                "name": "Comoros",
                "capital": "Moroni"
            },
            {
                "name": "Congo",
                "capital": "Brazzaville"
            },
            {
                "name": "Cook Islands",
                "capital": "Avarua"
            },
            {
                "name": "Costa Rica",
                "capital": "San José"
            },
            {
                "name": "Croatia",
                "capital": "Zagreb"
            },
            {
                "name": "Cuba",
                "capital": "La Habana"
            },
            {
                "name": "Cyprus",
                "capital": "Nicosia"
            },
            {
                "name": "Czech Republic",
                "capital": "Praha"
            },
            {
                "name": "Denmark",
                "capital": "Copenhagen"
            },
            {
                "name": "Djibouti",
                "capital": "Djibouti"
            },
            {
                "name": "Dominica",
                "capital": "Roseau"
            },
            {
                "name": "Dominican Republic",
                "capital": "Santo Domingo de Guzm"
            },
            {
                "name": "East Timor",
                "capital": "Dili"
            },
            {
                "name": "Ecuador",
                "capital": "Quito"
            },
            {
                "name": "Egypt",
                "capital": "Cairo"
            },
            {
                "name": "El Salvador",
                "capital": "San Salvador"
            },
            {
                "name": "England",
                "capital": "London"
            },
            {
                "name": "Equatorial Guinea",
                "capital": "Malabo"
            },
            {
                "name": "Eritrea",
                "capital": "Asmara"
            },
            {
                "name": "Estonia",
                "capital": "Tallinn"
            },
            {
                "name": "Ethiopia",
                "capital": "Addis Abeba"
            },
            {
                "name": "Falkland Islands",
                "capital": "Stanley"
            },
            {
                "name": "Faroe Islands",
                "capital": "Tórshavn"
            },
            {
                "name": "Fiji Islands",
                "capital": "Suva"
            },
            {
                "name": "Finland",
                "capital": "Helsinki [Helsingfors]"
            },
            {
                "name": "France",
                "capital": "Paris"
            },
            {
                "name": "French Guiana",
                "capital": "Cayenne"
            },
            {
                "name": "French Polynesia",
                "capital": "Papeete"
            },
            {
                "name": "French Southern territories",
                "capital": None
            },
            {
                "name": "Gabon",
                "capital": "Libreville"
            },
            {
                "name": "Gambia",
                "capital": "Banjul"
            },
            {
                "name": "Georgia",
                "capital": "Tbilisi"
            },
            {
                "name": "Germany",
                "capital": "Berlin"
            },
            {
                "name": "Ghana",
                "capital": "Accra"
            },
            {
                "name": "Gibraltar",
                "capital": "Gibraltar"
            },
            {
                "name": "Greece",
                "capital": "Athenai"
            },
            {
                "name": "Greenland",
                "capital": "Nuuk"
            },
            {
                "name": "Grenada",
                "capital": "Saint George's"
            },
            {
                "name": "Guadeloupe",
                "capital": "Basse-Terre"
            },
            {
                "name": "Guam",
                "capital": "Aga"
            },
            {
                "name": "Guatemala",
                "capital": "Ciudad de Guatemala"
            },
            {
                "name": "Guinea",
                "capital": "Conakry"
            },
            {
                "name": "Guinea-Bissau",
                "capital": "Bissau"
            },
            {
                "name": "Guyana",
                "capital": "Georgetown"
            },
            {
                "name": "Haiti",
                "capital": "Port-au-Prince"
            },
            {
                "name": "Heard Island and McDonald Islands",
                "capital": None
            },
            {
                "name": "Holy See (Vatican City State)",
                "capital": "Citt"
            },
            {
                "name": "Honduras",
                "capital": "Tegucigalpa"
            },
            {
                "name": "Hong Kong",
                "capital": "Victoria"
            },
            {
                "name": "Hungary",
                "capital": "Budapest"
            },
            {
                "name": "Iceland",
                "capital": "Reykjavík"
            },
            {
                "name": "India",
                "capital": "New Delhi"
            },
            {
                "name": "Indonesia",
                "capital": "Jakarta"
            },
            {
                "name": "Iran",
                "capital": "Tehran"
            },
            {
                "name": "Iraq",
                "capital": "Baghdad"
            },
            {
                "name": "Ireland",
                "capital": "Dublin"
            },
            {
                "name": "Israel",
                "capital": "Jerusalem"
            },
            {
                "name": "Italy",
                "capital": "Roma"
            },
            {
                "name": "Ivory Coast",
                "capital": "Yamoussoukro"
            },
            {
                "name": "Jamaica",
                "capital": "Kingston"
            },
            {
                "name": "Japan",
                "capital": "Tokyo"
            },
            {
                "name": "Jordan",
                "capital": "Amman"
            },
            {
                "name": "Kazakhstan",
                "capital": "Astana"
            },
            {
                "name": "Kenya",
                "capital": "Nairobi"
            },
            {
                "name": "Kiribati",
                "capital": "Bairiki"
            },
            {
                "name": "Kuwait",
                "capital": "Kuwait"
            },
            {
                "name": "Kyrgyzstan",
                "capital": "Bishkek"
            },
            {
                "name": "Laos",
                "capital": "Vientiane"
            },
            {
                "name": "Latvia",
                "capital": "Riga"
            },
            {
                "name": "LebaNone",
                "capital": "Beirut"
            },
            {
                "name": "Lesotho",
                "capital": "Maseru"
            },
            {
                "name": "Liberia",
                "capital": "Monrovia"
            },
            {
                "name": "Libyan Arab Jamahiriya",
                "capital": "Tripoli"
            },
            {
                "name": "Liechtenstein",
                "capital": "Vaduz"
            },
            {
                "name": "Lithuania",
                "capital": "Vilnius"
            },
            {
                "name": "Luxembourg",
                "capital": "Luxembourg [Luxemburg/L"
            },
            {
                "name": "Macao",
                "capital": "Macao"
            },
            {
                "name": "North Macedonia",
                "capital": "Skopje"
            },
            {
                "name": "Madagascar",
                "capital": "Antananarivo"
            },
            {
                "name": "Malawi",
                "capital": "Lilongwe"
            },
            {
                "name": "Malaysia",
                "capital": "Kuala Lumpur"
            },
            {
                "name": "Maldives",
                "capital": "Male"
            },
            {
                "name": "Mali",
                "capital": "Bamako"
            },
            {
                "name": "Malta",
                "capital": "Valletta"
            },
            {
                "name": "Marshall Islands",
                "capital": "Dalap-Uliga-Darrit"
            },
            {
                "name": "Martinique",
                "capital": "Fort-de-France"
            },
            {
                "name": "Mauritania",
                "capital": "Nouakchott"
            },
            {
                "name": "Mauritius",
                "capital": "Port-Louis"
            },
            {
                "name": "Mayotte",
                "capital": "Mamoutzou"
            },
            {
                "name": "Mexico",
                "capital": "Ciudad de M"
            },
            {
                "name": "Micronesia, Federated States of",
                "capital": "Palikir"
            },
            {
                "name": "Moldova",
                "capital": "Chisinau"
            },
            {
                "name": "Monaco",
                "capital": "Monaco-Ville"
            },
            {
                "name": "Mongolia",
                "capital": "Ulan Bator"
            },
            {
                "name": "Montenegro",
                "capital": "Podgorica"
            },
            {
                "name": "Montserrat",
                "capital": "Plymouth"
            },
            {
                "name": "Morocco",
                "capital": "Rabat"
            },
            {
                "name": "Mozambique",
                "capital": "Maputo"
            },
            {
                "name": "Myanmar",
                "capital": "Rangoon (Yangon)"
            },
            {
                "name": "Namibia",
                "capital": "Windhoek"
            },
            {
                "name": "Nauru",
                "capital": "Yaren"
            },
            {
                "name": "Nepal",
                "capital": "Kathmandu"
            },
            {
                "name": "Netherlands",
                "capital": "Amsterdam"
            },
            {
                "name": "Netherlands Antilles",
                "capital": "Willemstad"
            },
            {
                "name": "New Caledonia",
                "capital": "Noum"
            },
            {
                "name": "New Zealand",
                "capital": "Wellington"
            },
            {
                "name": "Nicaragua",
                "capital": "Managua"
            },
            {
                "name": "Niger",
                "capital": "Niamey"
            },
            {
                "name": "Nigeria",
                "capital": "Abuja"
            },
            {
                "name": "Niue",
                "capital": "Alofi"
            },
            {
                "name": "Norfolk Island",
                "capital": "Kingston"
            },
            {
                "name": "North Korea",
                "capital": "Pyongyang"
            },
            {
                "name": "Northern Ireland",
                "capital": "Belfast"
            },
            {
                "name": "Northern Mariana Islands",
                "capital": "Garapan"
            },
            {
                "name": "Norway",
                "capital": "Oslo"
            },
            {
                "name": "Oman",
                "capital": "Masqat"
            },
            {
                "name": "Pakistan",
                "capital": "Islamabad"
            },
            {
                "name": "Palau",
                "capital": "Koror"
            },
            {
                "name": "Palestine",
                "capital": "Gaza"
            },
            {
                "name": "Panama",
                "capital": "Ciudad de Panamá"
            },
            {
                "name": "Papua New Guinea",
                "capital": "Port Moresby"
            },
            {
                "name": "Paraguay",
                "capital": "Asunción"
            },
            {
                "name": "Peru",
                "capital": "Lima"
            },
            {
                "name": "Philippines",
                "capital": "Manila"
            },
            {
                "name": "Pitcairn",
                "capital": "Adamstown"
            },
            {
                "name": "Poland",
                "capital": "Warszawa"
            },
            {
                "name": "Portugal",
                "capital": "Lisboa"
            },
            {
                "name": "Puerto Rico",
                "capital": "San Juan"
            },
            {
                "name": "Qatar",
                "capital": "Doha"
            },
            {
                "name": "Reunion",
                "capital": "Saint-Denis"
            },
            {
                "name": "Romania",
                "capital": "Bucuresti"
            },
            {
                "name": "Russian Federation",
                "capital": "Moscow"
            },
            {
                "name": "Rwanda",
                "capital": "Kigali"
            },
            {
                "name": "Saint Helena",
                "capital": "Jamestown"
            },
            {
                "name": "Saint Kitts and Nevis",
                "capital": "Basseterre"
            },
            {
                "name": "Saint Lucia",
                "capital": "Castries"
            },
            {
                "name": "Saint Pierre and Miquelon",
                "capital": "Saint-Pierre"
            },
            {
                "name": "Saint Vincent and the Grenadines",
                "capital": "Kingstown"
            },
            {
                "name": "Samoa",
                "capital": "Apia"
            },
            {
                "name": "San Marino",
                "capital": "San Marino"
            },
            {
                "name": "Sao Tome and Principe",
                "capital": "São Tomé"
            },
            {
                "name": "Saudi Arabia",
                "capital": "Riyadh"
            },
            {
                "name": "Scotland",
                "capital": "Edinburgh"
            },
            {
                "name": "Senegal",
                "capital": "Dakar"
            },
            {
                "name": "Serbia",
                "capital": "Belgrade"
            },
            {
                "name": "Seychelles",
                "capital": "Victoria"
            },
            {
                "name": "Sierra Leone",
                "capital": "Freetown"
            },
            {
                "name": "Singapore",
                "capital": "Singapore"
            },
            {
                "name": "Slovakia",
                "capital": "Bratislava"
            },
            {
                "name": "Slovenia",
                "capital": "Ljubljana"
            },
            {
                "name": "Solomon Islands",
                "capital": "Honiara"
            },
            {
                "name": "Somalia",
                "capital": "Mogadishu"
            },
            {
                "name": "South Africa",
                "capital": "Pretoria"
            },
            {
                "name": "South Georgia and the South Sandwich Islands",
                "capital": None
            },
            {
                "name": "South Korea",
                "capital": "Seoul"
            },
            {
                "name": "South Sudan",
                "capital": "Juba"
            },
            {
                "name": "Spain",
                "capital": "Madrid"
            },
            {
                "name": "Sri Lanka",
                "capital": "Colombo, Sri Jayawardenepura Kotte"
            },
            {
                "name": "Sudan",
                "capital": "Khartum"
            },
            {
                "name": "Suriname",
                "capital": "Paramaribo"
            },
            {
                "name": "Svalbard and Jan Mayen",
                "capital": "Longyearbyen"
            },
            {
                "name": "Swaziland",
                "capital": "Mbabane"
            },
            {
                "name": "Sweden",
                "capital": "Stockholm"
            },
            {
                "name": "Switzerland",
                "capital": "Bern"
            },
            {
                "name": "Syria",
                "capital": "Damascus"
            },
            {
                "name": "Tajikistan",
                "capital": "Dushanbe"
            },
            {
                "name": "Tanzania",
                "capital": "Dodoma"
            },
            {
                "name": "Thailand",
                "capital": "Bangkok"
            },
            {
                "name": "The Democratic Republic of Congo",
                "capital": "Kinshasa"
            },
            {
                "name": "Togo",
                "capital": "Lomé"
            },
            {
                "name": "Tokelau",
                "capital": "Fakaofo"
            },
            {
                "name": "Tonga",
                "capital": "Nuku'alofa"
            },
            {
                "name": "Trinidad and Tobago",
                "capital": "Port-of-Spain"
            },
            {
                "name": "Tunisia",
                "capital": "Tunis"
            },
            {
                "name": "Turkey",
                "capital": "Ankara"
            },
            {
                "name": "Turkmenistan",
                "capital": "Ashgabat"
            },
            {
                "name": "Turks and Caicos Islands",
                "capital": "Cockburn Town"
            },
            {
                "name": "Tuvalu",
                "capital": "Funafuti"
            },
            {
                "name": "Uganda",
                "capital": "Kampala"
            },
            {
                "name": "Ukraine",
                "capital": "Kyiv"
            },
            {
                "name": "United Arab Emirates",
                "capital": "Abu Dhabi"
            },
            {
                "name": "United Kingdom",
                "capital": "London"
            },
            {
                "name": "United States",
                "capital": "Washington"
            },
            {
                "name": "United States Minor Outlying Islands",
                "capital": None
            },
            {
                "name": "Uruguay",
                "capital": "Montevideo"
            },
            {
                "name": "Uzbekistan",
                "capital": "Toskent"
            },
            {
                "name": "Vanuatu",
                "capital": "Port-Vila"
            },
            {
                "name": "Venezuela",
                "capital": "Caracas"
            },
            {
                "name": "Vetican City",
                "capital": "Vetican City"
            },
            {
                "name": "Vietnam",
                "capital": "Hanoi"
            },
            {
                "name": "Virgin Islands, British",
                "capital": "Road Town"
            },
            {
                "name": "Virgin Islands, U.S.",
                "capital": "Charlotte Amalie"
            },
            {
                "name": "Wales",
                "capital": "Cardiff"
            },
            {
                "name": "Wallis and Futuna",
                "capital": "Mata-Utu"
            },
            {
                "name": "Western Sahara",
                "capital": "El-Aai"
            },
            {
                "name": "Yemen",
                "capital": "Sanaa"
            },
            {
                "name": "Zambia",
                "capital": "Lusaka"
            },
            {
                "name": "Zimbabwe",
                "capital": "Harare"
            }
        ]