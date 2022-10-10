# SWE 2 Build an image carousel - Share with Candidate - Public

## Description

Build an image carousel component! It should have:
* An image actively being displayed
* Two buttons, one to move forward and one to move back

Display these images:

```
    const urls = [
        "https://images.pexels.com/photos/269255/pexels-photo-269255.jpeg",
        "https://images.pexels.com/photos/355235/pexels-photo-355235.jpeg",
        "https://images.pexels.com/photos/416179/pexels-photo-416179.jpeg"
    ]
```

## Links to Extra Files or References

Here is an (exceptional) example from Bootstrap just so the candidate gets an idea of what they're making.

https://mdbootstrap.com/docs/standard/components/carousel/

## Preparation Instructions to be Shared in Advance

Use either codepen or glider.

Share with candidate:

```
Please create a codepen account in advance and be prepared to use either React with classes
or React with Hooks.

Fork this codepen and have it open https://codepen.io/kieter/pen/poNNdjq before the
interview starts
```

# Intuit Internal ONLY Do Not Share with Candidate

Estimated time to complete: 15-20 minutes.

A strong candidate should be able to finish this relatively quickly. Here are some follow-up requirements:
* Center the component on the screen (ideally they use flexbox to do this rather than text-align)
* Give them some time to decorate the carousel
* Create an indicator beneath the carousel that informs them how many images there are, and which image they're on right now (typically done with three white dots, one being colored in and the other two not colored in but leaving this open lets them demonstrate their eye for design)

### Skills tested by this question
* React
* New react hooks (if they used them)
* React state management
* CSS
* Some data manipulation

### Common Clarification Questions/FAQ
The candidate might initially be flustered by the task, I've noticed this before. Just remind them that it's just an image and two buttons.

Outside of this it should go relatively smoothly.

## Solution

### Approach:

As for most UI work, ideally they start by putting the components on the page so that 1. They can ensure their environment works and 2. they can properly place their images and buttons.

But here's an ideal approach:
1. Candidate asks any clarifying questions
2. Draws out or thinks about their approach, explaining it in words before coding right away.
3. Renders the image as well as the buttons.
4. Organizes the given images into state
5. Creates a variable to track the index of the image being displayed
6. Writes TWO separate handlers for the left and right button
7. Makes the component pretty by centering it and adding some CSS

Catches:
* Over-engineering a single handler for both buttons.
* Centering using text-align rather than flex (ask them to render two and center both in the same container without adding more CSS)
* Candidate is does not think through the problem before coding.
* If the handlers they write assume there's only 3 images

### Sample Solution
https://codepen.io/kieter/pen/QWGGOdJ

### Time complexity

N/A, not a huge amount of processing being done here. Ideally the handlers for the buttons switching images aren't overly complex though.

### How to Assess Candidate

Generally this problem should only be used for SWE2.

A strong candidate should be able to solve this relatively quickly, giving some indication that they do UI work regularly and aren't totally lost nor guessing when it comes to CSS. If they're given time to decorate the component, ideally it looks modern, something you'd be able to put on a website today.

### Variation/Similar Problem

Not very extensible outside of front end. If you want to make a more complex question, include all of the extras noted above.

## Additional notes

This question should be relatively easy for someone who does UI work every day or regularly. They're given the data up front so there's no need for them to figure out what kind of data structure to use (since the back end will give it to them anyway in a real life situation). If you're really looking for CSS aptitude, this is an excellent question if you include all the extras.

## Tags

`easy`, `phonescreen`, `swe2`, `frontend`, `css`, `react`
