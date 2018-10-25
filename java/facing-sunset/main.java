import java.util.Arrays;
import java.io.*;


class Main {
  public static void main(String[] args) {
    
    try{ 
      // to read the contents of the file
          BufferedReader br = new BufferedReader(new FileReader("test.txt"));
          int testCases = Integer.parseInt(br.readLine());

          while(testCases > 0){
            // Determine number of buildings
            // Convert the string to a int array
            int numBuildings = Integer.parseInt(br.readLine());
            int[] buildings = convertToIntArray(br.readLine(), numBuildings);
            determineFacingSunset(buildings);

            testCases--;
          } 
          
    }catch(IOException e){
      System.out.println("An exception was thrown, we could no find the file you were searching for.");
    }
  }


  // determine the number of buildings facing the sunset
  public static void determineFacingSunset(int[] buildings){
    int facingSunset = 1;
    int maxHeight = buildings[0];
    for(int i = 1; i < buildings.length; i++){
      if(buildings[i] == maxHeight){
        facingSunset++;
      }else if(buildings[i] > maxHeight){
        facingSunset++; 
        maxHeight = buildings[i]; // set new max height
      }
    }
    System.out.println(facingSunset);
  }


  // Converts a string array to 
  public static int[] convertToIntArray(String buildings, int numBuildings){
    // Convert string to string array using a space delimiter
    String[] buildingStrArr = buildings.split(" ");
    int[] buildingsIntArr = new int[numBuildings];

    for(int i = 0; i < numBuildings; i++){ 
      buildingsIntArr[i] = Integer.parseInt(buildingStrArr[i]);
    }
    
    return buildingsIntArr;
  }
}



