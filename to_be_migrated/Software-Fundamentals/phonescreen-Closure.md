# Suited For

Software Engineer 2 and/or Senior Software Engineer

## Difficulty Level

`medium`

### Given Problem Statement

Describe a closure and create an example. Estimated time to complete: 10 minutes

### Tags

Tags: software medium fundamental language-independent

### Description

Closures are implemented in many programming languages (particularily in functional languages) and provide a very important engineering capability.  Can you explain what a closure is, where they could be used and then code up an example of a closure that implements a simple counter?

### Approach:

The simplest approach would be to use Javascript with HTML to demonstrate the capability.

### Sample Solution:

<!DOCTYPE html>
<html>
<body>
<button type="button" onclick="myFunction()">Increment</button>
<p id="demo"></p>
<script>
var x = 0;
document.getElementById("demo").innerHTML = x;
function myFunction() {
  x = x + 1;
  document.getElementById("demo").innerHTML = x;
}
</script>
</body>
</html>
