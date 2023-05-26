Feature: calculation

    Scenario: PlusCalculate
        Given 5, 4, operator 
        When operator is + 
        Then return 9 

    Scenario: MinusCalculate
        Given 7, 4, operator 
        When operator is - 
        Then return 3  

    Scenario: DivideCalculate
        Given 6, 3, operator 
        When operator is / 
        Then return 2 

    Scenario: MultiplyCalculate
        Given 100, 50, operator 
        When operator is * 
        Then return 5000 

    Scenario: ModulusCalculate
        Given 10, 3, operator 
        When operator is % 
        Then return 1

 