"""
Module for connections between neural populations.
"""

from abc import ABC, abstractmethod
from typing import Union, Sequence

import torch
from torch.nn import Module, Parameter

from .neural_populations import NeuralPopulation


class AbstractConnection(ABC, torch.nn.Module):
    """
    Abstract class for implementing connections.

    Make sure to implement the `compute`, `update`, and `reset_state_variables`\
    methods in your child class.

    You will need to define the populations you want to connect as `pre` and `post`.\
    Attribute `w` is reserved for synaptic weights.\
    However, it has not been predefined or allocated, as it depends on the \
    pattern of connectivity. So make sure to define it in child class initializations \
    appropriately to indicate the pattern of connectivity. The default range of \
    each synaptic weight is [0, 1] but it can be controlled by `w_min` and `w_max`. \
    Also,  if you want to control the overall input synaptic strength to each neuron, \
    use `norm` argument to normalize the synaptic weights.

    In case of learning, you have to implement the methods `compute` and `update`. \
    You will use the `compute` method to calculate the activity of post-synaptic \
    population based on the pre-synaptic one. Update of weights based on the \
    learning rule will be implemented in the `update` method. If you find this \
    architecture mind-bugling, try your own architecture and make sure to redefine \
    the learning rule architecture to be compatible with this new architecture \
    of yours.

    Arguments
    ---------
    pre : NeuralPopulation
        The pre-synaptic neural population.
    post : NeuralPopulation
        The post-synaptic neural population.
    w:  Tensor
        The tensor of weights for the connection.
    d: Tensor
       The tensor of delays for the connection.
    d_min: float
        The minimum possible delay. The default is 0.0.
    d_max: float
        The maximum possible delay. The default is 100.
    mask:  ByteTensor
        Define a mask to determine which weights to clamp to zero.

    Keyword Arguments
    -----------------
    
    w_min : float
        The minimum possible synaptic strength. The default is 0.0.
    w_max : float
        The maximum possible synaptic strength. The default is 1.0.
    norm : float
        Define a normalization on input signals to a population. If `None`,\
        there is no normalization. The default is None.
    b: Tensor
        bias parameter
    """

    def __init__(
        self,
        pre: NeuralPopulation,
        post: NeuralPopulation,
        w: torch.Tensor,
        d: torch.Tensor,
        d_min: float = 0.0,
        d_max: float = 100.0,
        mask: torch.ByteTensor = True,
        **kwargs
    ) -> None:
        super().__init__()

        assert isinstance(pre, NeuralPopulation), \
            "Pre is not a NeuralPopulation instance"
        assert isinstance(post, NeuralPopulation), \
            "Post is not a NeuralPopulation instance"

        self.pre = pre
        self.post = post

        self.w = w

        self.w_min = kwargs.get('w_min', torch.zeros(pre.n, post.n))
        self.w_max = kwargs.get('w_max', torch.ones(pre.n, post.n))
        self.norm = kwargs.get('norm', None)
        
        self.d_min = d_min
        self.d_max = d_max
        """
        define memories to save sequence of weights and delays for spikes.  
        """
        self.delay_mem = torch.Tensor([])
        self.w_mem = torch.Tensor([])

    @abstractmethod
    def compute(self, s: torch.Tensor) -> None:
        """
        Compute the post-synaptic neural population activity based on the given\
        spikes of the pre-synaptic population.

        Parameters
        ----------
        s : torch.Tensor
            The pre-synaptic spikes tensor.

        Returns
        -------
        None

        """
        pass

    @abstractmethod
    def update(self, **kwargs) -> None:
        """
        Compute connection's learning rule and weight update.

        Keyword Arguments
        -----------------
        learning : bool
            Whether learning is enabled or not. The default is True.
        mask : torch.ByteTensor
            Define a mask to determine which weights to clamp to zero.

        Returns
        -------
        None

        """
        pass
    @abstractmethod
    def reset_state_variables(self) -> None:
        """
        Reset all internal state variables.

        Returns
        -------
        None

        """
        pass
    
class Connection(AbstractConnection):
    def __init__(
        self,
        pre: NeuralPopulation,
        post: NeuralPopulation,
        w: torch.Tensor = None,
        d: torch.Tensor = None,
        d_min: float = 0.0,
        d_max: float = 100.0,
        mask: torch.ByteTensor = True,
        **kwargs
    ) -> None:
        super().__init__(
            pre = pre,
            post = post,
            w = w,
            d = d,
            d_min = d_min,
            d_max = d_max,
            mask = mask
        )

        if w is None:
            if (self.w_min == float('-inf')).any() or (self.w_max == float('inf')).any():
                w = torch.clamp(torch.rand(pre.n, post.n), self.w_min, self.w_max)
            else:
                w = self.w_min + torch.rand(pre.n, post.n) * (self.w_max - self.w_min)
        else:
            if (self.w_min != float('-inf')).any() or (self.w_max != float('inf')).any():
                w = torch.clamp(torch.as_tensor(w), self.w_min, self.w_max)

        if d is None:
            if (self.d_min == 0.0) or (self.d_max == float('inf')):
                d = torch.clamp(torch.rand(pre.n, post.n), self.d_min, self.d_max)
            else:
                d = self.d_min + torch.rand(pre.n, post.n) * (self.d_max - self.d_min)
        else:
            if (self.d_min != 0.0) or (self.d_max != float('inf')):
                d = torch.clamp(torch.as_tensor(d), self.d_min, self.d_max)     

        self.w = Parameter(w, requires_grad=False)
        self.d = Parameter(d, requires_grad=False)

        b = kwargs.get("b", None)
        if b is not None:
            self.b = Parameter(b, requires_grad=False)
        else:
            self.b = None

    def compute(self, s: torch.Tensor) -> torch.Tensor:
        """
        Compute the post-synaptic neural population activity based on the given\
        spikes of the pre-synaptic population.

        Parameters
        ----------
        s : torch.Tensor
            The pre-synaptic spikes tensor.

        Returns
        -------
        None

        """

        self.delay_mem = torch.cat((self.delay_mem, torch.masked_select(self.d, s.bool())), 0)
        self.w_mem = torch.cat((self.w_mem, torch.masked_select(self.w, s.bool())), 0)

        exp = self.delay_mem <= 0
        w_result = self.w_mem.dot(exp.float())

        self.w_mem = torch.masked_select(self.w_mem, torch.logical_not(exp))
        self.delay_mem = self.delay_mem > 0
        

        if self.b is None:
            result = torch.ones(s.size(0), *self.post.shape) * w_result
        else:
            result = torch.ones(s.size(0), *self.post.shape) * w_result + self.b 

        return result  
        #return torch.ones(s.size(0), *self.post.shape) * w_result

    def reset_state_variables(self) -> None:
        """
        Contains resetting logic for the connection.
        """
        super().reset_state_variables()

    def normalize(self) -> None:
        # language=rst
        """
        Normalize weights so each target neuron has sum of connection weights equal to
        ``self.norm``.
        """
        if self.norm is not None:
            w_abs_sum = self.w.abs().sum(0).unsqueeze(0)
            w_abs_sum[w_abs_sum == 0] = 1.0
            self.w *= self.norm / w_abs_sum
    def update(self, **kwargs) -> None:
        # language=rst
        """
        Compute connection's update rule.
        """
        super().update(**kwargs)