# Nameko Learning - Invictus
For Invictus Assessment
## The Task
### Overview 
 - I think it's a fair assessment for the position advertised. 
 - Tests the rate of learning rather than already kept knowledge.
 - The Nameko framework wasn't the easiest to research though. There's much about it in the wild.This means you spend a lot of time , learning how to aspects of it to come together instead of using it. Time spent learning the tool more than using it.
### Nameko Pros
 - Easy to setup after fighting thorugh python versions and missing modules.
 - Easily testable through pytest
 - Comes with a preset AMQP in rabbitmq
 - Easy to test your service during development within the shell
### Nameko Cons
 - Not widely used, so scarce resources in terms of simple research. Popularity lacks a bit, so if you're stuck you might be alone for a while, even with their discussion/forum community.
 - Not enough and laid out examples in their documentaion. So you have to pick up bits and pieces from everywhere and hope that they'll fit together.
 - Doesn't explicitly specify the versions of python or other modules needed. Found out that it's less buggy for versions released a bit after 2.7.14 through some pain.
 
### Decisions made in design
 - Took the service file to a `src` directory to follow popular software design setups
 - Imported a python module to help in creating a huffman string indexed dict for the secodn task. This just eases the pain of encoding manually
 - Using a bash script to tie everything together when building the Docker container
 - Leveraging pytest for unit testing, because Nameko already endorses it.
 - 
## Time Spent in Research
- Just an FYI: I only managed to spent two nights on this. Rough working weekend. Didn't have much time to peek thorugh. 
### Nameko 
- Of the two nights, I think just getting to grips with Nameko and what it is took a little bit of time. In that all you know is the little the given in the documentation. The rest I had scour the not so dark corners of the internet to find and see how people actually use it, and how everything comes together. (So maybe 2-3hours)
- Python versions. Had to pyenv and virtualenv a bit to see why it didn't like some versions. Wasted some minutes on this. Wasted my own time really. (About and hour and a half)
- 
### Huffman Encoding
 - Didn't really understand what huffman encoding was really about, so took a bit of time trying to see what that was about. And how the python community uses it and when. A bit tough to do, eventually realised that people only really use this in algorithm tests and such. So explanations were a bit scarce. (2-3hours)
 - 
### Writing the code and trying to put it all together
  - This was a bit touch and go, since everything was just experimenting to see what happens after you've written something (3 - 5hours)
  - 
 ### Creating and the Dockerfile and testing the Container
 - Strugled a bit trying to get rabbitmq to speak to the setup before I understood how the connect to each other (3 - hours)
 - Was odd building a service that went full RPC instead of some HTTP. Getting used to this paradagm was a little odd at the beginning :). But eventually I start riding the bicycle. (2 hours)
 - 

