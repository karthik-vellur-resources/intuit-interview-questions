# Weather Statistics

## Tags

Level Options: `swe2`, `sse`, `staff`

Role Category: `backend`

Difficulty Options: `medium`

Interview Type Options: `phonescreen` `onsite` `craft-demo`  

## Share with Candidate - Public

### Description
Design and implement a method which returns Top K cities for a given weather attribute.

`attributes:`

pressure, humidity, temp


### Preparation Instructions to be shared with the candidate.

* You can use any programming language & IDE of your choice
* Your method should take a list of WeatherData objects. The output should be an object of type TopK. WeatherData and TopK data model is described as below.
* The data types of weather stats are as specified in the data model.

#### Data Preparation

Input data object
```json
    {
        "id": "1",
        "name": "London",
        "temp": 14,
        "pressure": 15,
        "humidity": 51
    }
```
for example:

Input data model (WeatherData)
```java
public static class WeatherData {
        private int id;
        private String city;
        private int temp;
        private int pressurePsi;
        private int humidity;
        
        public WeatherData(int id, String city, int temp, int pressure, int humidity) {
            this.id = id;
            this.city = city;
            this.temp = temp;
            this.pressurePsi = pressure;
            this.humidity = humidity;
        }
        
        public String getCityName() {
            return this.city;
        }
        
        public int getTemp() {
            return this.temp;
        }
        
        public int getPressure() {
            return this.pressurePsi;
        }
        
        public int getHumidity() {
            return this.humidity;
        }

        @Override
        public String toString() {
            return "Weather={" +
                    "city='" + city + '\'' +
                    "temp=" +  temp + '\'' +
                    "humidity=" +  humidity + '\'' +
                    '}';
        }
        
    }

```

Input data model (TopK)
```java
public static class TopK {
        private int k;
        private String stat;
        private List<WeatherData> dataList;
        
        public TopK(int k, String stat, List<WeatherData> dataList) {
            this.k = k;
            this.stat = stat;
            this.dataList = dataList;
        }
        
        public List<WeatherData> getDataList() {
            return this.dataList;
        }
    }
```
## Intuit Internal ONLY Do Not Share with Candidate

### Estimated time to complete
* ~ 15-20 minutes to come up with a design
* ~ 30 minutes to code

### Common Clarification Questions/FAQ

* Should the design efficiently solve for selecting Top K items or should it efficiently solve for caching weather data?
`The design should efficiently solve for selecting top K items`
**Good question as a potential SSE. Interviewer can discuss pros & cons of the design if time permits. **

### Solution

#### Approach

Depending on skill and experience level of the candidate , the solution to problem (and subsequent interview Q&A) can span multiple paths. As such interviewer can calibrate the response to increase progessive complexity of questioning trying to draw candidate to "stretch" zone

`Core business logic` - 
*How to efficienty select Top K items in a large list of objects based on a dynamic predicate*

1. **Brute Force:** Sort and select top k
    - Time complexity to sort data: O(nlogn)
    - Time complexity to select top k =  O(k)

2. **Heap Select** - Heapify the objects , based on stat predicate, and select top k.
    - Build a Max Heap tree in O(n) 
    - Use Extract Max k times to get k maximum elements from the Max Heap O(klogn)
    - Time complexity: O(n + klogn)

3. **Order statistics using Quickselect algorithm**  https://en.wikipedia.org/wiki/Quickselect
    - Use QuickSort Partition algorithm to partition around the kth largest number: O(n). 
    - Sort the k-1 elements (elements greater than the kth largest element) O(kLogk). This step is needed only if sorted output is required.
    - Time complexity: O(n) if we don’t need the sorted output, otherwise O(n+kLogk)


Depending on approach taken, Can candidate articulate the algorithmic complexities , both space and time, for approaches above ?

### Testing
- If candidate exhibits basic TDD in API writing, that is great
- At the least, candidate should be able to talk through top negative/edge test cases
- Bonus points for writing or articulating Benchmarking tests to evaluate algorithm approaches

### Sample Solution (works as is in glider)

```java
import java.util.*;

class WeatherStats {

    public WeatherStats() {}
    
    /* Solution using PQ */
    private TopK getTopKDataByTemp(int k, List<WeatherData> inputList) {
        
        /* initialize PQ with temp comparator */
        PriorityQueue<WeatherData> tempQ = new PriorityQueue(new TempComparator());
        
        /* add all city data in PQ */
        for(WeatherData cityData : inputList) {
            tempQ.add(cityData);
        }
        
        List<WeatherData> result = new ArrayList<>();
        
        while(k > 0) {
            WeatherData city = tempQ.poll();
            result.add(city);
            k--;
        }
        
        return new TopK(k, "TEMP", result);
    }
    
    
    /* Solution using sort + select */
    private TopK getTopKDataByHumidity(int k, List<WeatherData> inputList) {
        
        /* Sort data */
        Collections.sort(inputList, new HumidityComparator());
        
        /* select data */
        List<WeatherData> result = new ArrayList<>();
        for(int i = 0; i < k; i++) {
            result.add(inputList.get(i));
        }
        
        return new TopK(k, "HUMIDITY", result);
    }
    /* core business logic */
    public TopK getTopKDataByStat(int k, String stat, List<WeatherData> inputList) throws Exception {
    
        /* Basic validation */
        if(k < 0 || k > inputList.size()) {
            throw new Exception("Invalid k value");
        }
        
        TopK topk = null;
        
        switch(stat) {
            case "temp":
                topk = getTopKDataByTemp(k, inputList);
                break;
            case "humidity":
                topk = getTopKDataByHumidity(k, inputList);
                break;
            default:
                throw new Exception("Invalid stat key");
        }
        
        return topk;
    } 
    

    /* Output data model */
    public static class TopK {
        private int k;
        private String stat;
        private List<WeatherData> dataList;
        
        public TopK(int k, String stat, List<WeatherData> dataList) {
            this.k = k;
            this.stat = stat;
            this.dataList = dataList;
        }
        
        public List<WeatherData> getDataList() {
            return this.dataList;
        }
    }
    
    /*  Temperature comparator. You can create comparators for other stats */
    public static class TempComparator implements Comparator<WeatherData> {
              
            /* Overriding compare() method of Comparator for descending order of temp */
            public int compare(WeatherData c1, WeatherData c2) {
                if (c1.getTemp() < c2.getTemp())
                    return 1;
                else if (c1.getTemp() > c2.getTemp())
                    return -1;
                
                return 0;
        }
    }
    
    /* Humidity comparator */
    public static class HumidityComparator implements Comparator<WeatherData> {
              
            /* Overriding compare() method of Comparator for descending order of humidity */
            public int compare(WeatherData c1, WeatherData c2) {
                if (c1.getHumidity() < c2.getHumidity())
                    return 1;
                else if (c1.getHumidity() > c2.getHumidity())
                    return -1;
                
                return 0;
        }
    }
    
    /* Input data model */
    public static class WeatherData {
        private int id;
        private String city;
        private int temp;
        private int pressurePsi;
        private int humidity;
        
        public WeatherData(int id, String city, int temp, int pressure, int humidity) {
            this.id = id;
            this.city = city;
            this.temp = temp;
            this.pressurePsi = pressure;
            this.humidity = humidity;
        }
        
        public String getCityName() {
            return this.city;
        }
        
        public int getTemp() {
            return this.temp;
        }
        
        public int getPressure() {
            return this.pressurePsi;
        }
        
        public int getHumidity() {
            return this.humidity;
        }

        @Override
        public String toString() {
            return "Weather={" +
                    "city='" + city + '\'' +
                    "temp=" +  temp + '\'' +
                    "humidity=" +  humidity + '\'' +
                    '}';
        }
        
    }

    public static void main(String[] args) {
        
        List<WeatherData> inputList = new ArrayList<>();
        
        /* Data setup */
        WeatherData mumbai = new WeatherData(1, "mumbai", 28, 14, 85);
        inputList.add(mumbai);
        WeatherData tokyo = new WeatherData(2, "tokyo", 26, 11, 12);
        inputList.add(tokyo);
        WeatherData seoul = new WeatherData(3, "seoul", 24, 12, 50);
        inputList.add(seoul);
        WeatherData seattle = new WeatherData(4, "seattle", 14, 8, 20);
        inputList.add(seattle);
        WeatherData chicago = new WeatherData(5, "chicago", 2, 14, 21);
        inputList.add(chicago);
        WeatherData paris = new WeatherData(6, "paris", 18, 15, 34);
        inputList.add(paris);
        WeatherData london = new WeatherData(7, "london", 19, 14, 51);
        inputList.add(london);
        WeatherData rome = new WeatherData(8, "rome", 25, 18, 60);
        inputList.add(rome);
        WeatherData auckland = new WeatherData(7, "auckland", 7, 10, 15);
        inputList.add(auckland);
        WeatherData moscow = new WeatherData(8, "moscow", -1, 12, 5);
        inputList.add(moscow);
        
        
        WeatherStats ws = new WeatherStats();
        
        try {
            
            TopK tempTopk = ws.getTopKDataByStat(5, "temp", inputList);
            TopK humidityTopK = ws.getTopKDataByStat(5, "humidity", inputList);
    
            System.out.println(" ********* TEMP ********** ");
            for(WeatherData city : tempTopk.getDataList()) {
                System.out.println(city.toString());
            }
        
            System.out.println(" ********* HUMIDITY ********** ");
            for(WeatherData city : humidityTopK.getDataList()) {
                System.out.println(city.toString());
            }
            
            // TopK exceptionTest = ws.getTopKDataByStat(50, "humidity", inputList);  //  Expected exception: "Invalid k value"
            
        } catch(Exception e) {
            System.out.println("Exception caught: " + e.toString());
        }
        
    }
}
```

OUTPUT
```
********* TEMP **********
Weather={city='mumbai'temp=28'humidity=85'}
Weather={city='tokyo'temp=26'humidity=12'}
Weather={city='rome'temp=25'humidity=60'}
Weather={city='seoul'temp=24'humidity=50'}
Weather={city='london'temp=19'humidity=51'}

********* HUMIDITY ********** 
Weather={city='mumbai'temp=28'humidity=85'}
Weather={city='rome'temp=25'humidity=60'}
Weather={city='london'temp=19'humidity=51'}
Weather={city='seoul'temp=24'humidity=50'}
Weather={city='paris'temp=18'humidity=34'}
```



### How to Assess Candidate / Expected Answer by Level

* A __SWE-2__ candidate should be able to:

    - Ask clarifying questions regarding the units for the weather stats and other edge cases.
    - Should be able to implement the method for the core business logic.
    - Should be able to converge on the brute force solution within 20 minutes and show progress towards optimal solution with hints.
    - Should be able to correctly identify time complexity of their solution.
    - Clear, organized code using the appropriate data structures, code reuse, appropriate class and 
     methods definitions, exception handling and logging.

* A __Senior__ candidate should be able to:

    - All expectations of SWE2.
    - Ask enough clarifying questions to determine the algorithm of choice.
    - Should be able to utilize the input & output data models in their code.
    - Should be able to write the comparators for stats.
    - Should identify appropriate exceptions ask clarifying questions regarding how to handle them.
    - Clear, organized code using the appropriate data structures, code reuse, appropriate class and 
     methods definitions, exception handling and logging.
    - Should be able to run their code and test with some sample data.

* A __Staff__ candidate should be able to: 
    - All expectations of Senior.
    - Design elegant and scalable solution.
    - Able to identify edge cases and resolve them creatively.

Also, questions that we would like the candidate to ask are also useful.
Edge cases identified, etc.


## References
* [Find top K efficiently](http://stevehanov.ca/blog/index.php?id=122)
* [Wikipedia - Quickselect](https://en.wikipedia.org/wiki/Quickselect)
