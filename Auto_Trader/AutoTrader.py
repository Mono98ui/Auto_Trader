from DataExtractor.Extractor import Extractor


def main():

    data = Extractor()
    # analyse the basic link first
    data.extract_brands()

    # After choosing the brand,
    # data.extract_model()

    # Then, choose the year
    # data.extract_years()

    # At the end...
    # total = data.extract_data()
    # print(total)


if __name__ == '__main__':
    main()
