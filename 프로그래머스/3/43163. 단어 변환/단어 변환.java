import java.util.Queue;
import java.util.LinkedList;
import java.util.Set;
import java.util.HashSet;

class Record{
    String word;
    int counter;
    
    public Record(String word, int counter){
        this.word = word;
        this.counter = counter;
    }
}

class Solution {
    public int solution(String begin, String target, String[] words) {
        // D.S.
        Queue<Record> q = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        
        // start
        q.add(new Record(begin, 0));
        visited.add(begin);
        int answer = 0;
        
        
        // bfs
        while(!q.isEmpty()){
            Record curr = q.poll();
            String cWord = curr.word;
            int cCounter = curr.counter;
            
            for(int i = 0 ; i<words.length; i++){
                
                if(!visited.contains(words[i]) && isConnected(cWord, words[i])){
                    cCounter++;
                    
                    // end condition => found.
                    if(words[i].equals(target)) return cCounter;
                    
                    visited.add(words[i]);
                    q.add(new Record(words[i], cCounter));
                }
            }
            
        }
       
        return 0; // end condition => not found.
    }
    
    public boolean isConnected(String src, String des){
        int sum = 0;
        for(int i=0; i<src.length(); i++){
           if(src.charAt(i) != des.charAt(i)) sum +=1;
        }
        
        return sum==1;
    }
}