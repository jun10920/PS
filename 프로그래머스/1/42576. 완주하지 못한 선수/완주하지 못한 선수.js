function solution(part, comp) {
    
    part.sort();
    comp.sort();
    
    for (let i = 0; i < part.length; i++) {
        if (part[i] != comp[i]) {
            return part[i];
        }
    }
    return comp[comp.length - 1]
}