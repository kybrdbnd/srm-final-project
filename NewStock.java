/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package NewStock;

import java.io.*;
import java.math.BigDecimal;
import java.net.URL;
import java.net.URLConnection;
import java.text.ParseException;
import java.util.Arrays;
import java.util.Calendar;

import java.util.List;
import java.util.Locale;
import javax.jws.soap.SOAPBinding;
import javax.jws.soap.SOAPBinding.Style;
import org.neuroph.core.NeuralNetwork;
import org.neuroph.core.data.DataSet;
import org.neuroph.core.data.DataSetRow;
import org.neuroph.nnet.MultiLayerPerceptron;
import org.neuroph.util.data.norm.MaxMinNormalizer;
import yahoofinance.Stock;
import yahoofinance.YahooFinance;
import yahoofinance.histquotes.HistoricalQuote;
import yahoofinance.quotes.stock.StockStats;

/**
 *
 * @author acer
 */
public class NewStock {
    
  static String  sym ;
  static double Reverse_Closing_price [] = new double[12];
  static List<HistoricalQuote> ls;
  static double [] closingPrice= new double[12];
  static double max,min;
  static int win1,win2;
  static int j,k,l;
 double output;
    public static void main(String [] args) throws ParseException, IOException {
       System.out.println("Enter NYSE ticker name only: for ex- FB/AAPL/GOOG/GOOGL/ABBV/ANF/ etc");
   BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
     sym =  br.readLine();
         Stock s = YahooFinance.get(sym);
         MaxMinNormalizer ff = new MaxMinNormalizer();
      ls = s.getHistory();
     for(int i=0;i<ls.size();i++)
     {    if(i<12)
     closingPrice[i]= ls.get(i).getClose().doubleValue();
     
     }
     max= closingPrice[0];
     for(int i=1;i<12;i++){
         if(max<closingPrice[i]){
          max= closingPrice[i];
         }
     }
     
     min = closingPrice[0];
     for(int i=1;i<12;i++){
         if(min>closingPrice[i]){
          min= closingPrice[i];
         }
     }
     //Reversing Closing Price Array
     for(int p=0;p<12;p++){
       int q=11-p;
       Reverse_Closing_price[p]= closingPrice[q];
     }
     
       for(int p=0;p<12;p++){
       
        closingPrice[p]=Reverse_Closing_price[p];
       
     }
       
     
      DataSet set = new DataSet(3,1);
      for(int i=0;i<closingPrice.length-3;i++){
         j=i+1;
         k=j+1;
         l=k+1;
         set.addRow(new double[]{closingPrice[i],closingPrice[j],closingPrice[k]}, new double[]{closingPrice[l]});
      }
      System.out.println("Avg.Monthly Closing Prices for   "+sym);
     
        for(int i=0;i<closingPrice.length;i++){
        System.out.println(closingPrice[i]+" "+ls.get(11-i).getDate().getTime().toString());
        // set.addRow(new double[]{closingPrice[i],closingPrice[j],closingPrice[k]}, new double[]{closingPrice[l]});
      }
      ff.normalize(set);
      System.out.println("Normalised Input Training Set");
      for(int o=0;o<set.size();o++)
      System.out.println(set.getRows().get(o));
      MultiLayerPerceptron mlp = new MultiLayerPerceptron(3,4,3,1);
      mlp.learn(set);
      DataSet input = new DataSet(3);
      
      input.addRow(new double[]{(closingPrice[j]-min)/(max-min),(closingPrice[k]-min)/(max-min),(closingPrice[l]-min)/(max-min)});
      //System.out.println("NaN: "+input.getRows());
      
     // ff.normalize(input);
      System.out.println("NaN: -------"+input.getRows());
      System.out.println("Testing Neural Network");
      testNeuralNetwork(mlp, set);
      System.out.println("Predicting next month closing value:");
    
      testNeuralNetwork(mlp,input);
      
     int number_of_layers = mlp.getLayers().length;
   
     int input_count = mlp.getInputsCount();
     int output = mlp.getOutputsCount();
     System.out.println("Neural Netwok Details\n"+"Number_of_inputs = "+input_count+"\n"+"Number_of_outputs "+output+"\n");
     System.out.println("Learning Rule Used is "+mlp.getLearningRule().toString()+" and Learning Rate is "+   mlp.getLearningRule().getLearningRate());
    
    
        
        
     
    }
   public static void testNeuralNetwork(NeuralNetwork nnet, DataSet testSet) {

for(DataSetRow dataRow : testSet.getRows()) {
nnet.setInput(dataRow.getInput());
nnet.calculate();

double[] networkOutput = nnet.getOutput();
double output = networkOutput[0]*(max-min)+min ;

System.out.print("Input: " + Arrays.toString(dataRow.getInput()) );
System.out.println(" Normalized Output: " + Arrays.toString(networkOutput) );
System.out.println(" Estimated Stock Price for Next Month " + output );
}}


        
    }

