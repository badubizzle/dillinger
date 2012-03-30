# Dillinger

Dillinger is a simple demonstration of how Tornado can use ZeroMQ. 

The ZMQ stream integrates with Tornado using Tornado's IOStream which gives us nonblocking ZMQ sockets for Tornado. Sweet!


## Setting It Up

We have to patch Tornado's ioloop to use the one provided by ZMQ. The provided `surgery.py` script will do that.

You can either download a clean copy of Tornado, which is a submodule of this repo, or you can setup a virtualenv.


### Clean Copy

Tornado is a submodule of this repo. You can run the following command to get the source and then play with this project inside this directory.

    $ git submodule update --init
    $ env PYTHONPATH="." ./surgery.py
    
    
### VirtualEnv

Just run surgery on it's own.

    $ ./surgery.py
    

## Trying It
    
*If you used `env PYTHONPATH="."` above, please use it for both scripts mentioned below.*

Once that's done, turn on `zmqnado.py`. This is the web front-end and is similar to how you'd write your own request handlers.

I provide a `fake_worker.py` as a very basic example of what a worker could look like.
