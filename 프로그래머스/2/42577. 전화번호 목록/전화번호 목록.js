function solution(pb) {
    
    pb.sort();
    for (let i = 0 ; i < pb.length - 1; i++) {
        if(pb[i + 1].startsWith(pb[i])){
            return false
        }
    }
    
    return true;
}