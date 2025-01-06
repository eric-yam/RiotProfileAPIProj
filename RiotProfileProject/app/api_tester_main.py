from api_test import APITest
class APITesterMain:
    def main():
        test = APITest()        
        print(test.get_puuid())
        print(test.get_top_champs())

    if __name__=="__main__":
        main()