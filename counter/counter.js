/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let val = -1
    return function() {
        val+=1
        return n + val
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */