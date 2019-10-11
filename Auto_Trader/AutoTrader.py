from DataExtractor.Extractor import Extractor


def main():

    data = Extractor()
    # analyse the basic link first
    brands = data.extract_brands()

    # After choosing the brand,
    data.extract_model(brands)

    # Then, choose the year
    # data.extract_years()

    # At the end...
    # total = data.extract_data()
    # print(total)


if __name__ == '__main__':
    main()
