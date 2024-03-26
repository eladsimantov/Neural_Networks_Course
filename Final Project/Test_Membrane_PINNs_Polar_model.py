"""
This script is to test a saved model of type Membrane Pinns. 
It assumes it is already trained and plots the outputs
"""
import torch
from Membrane_PINNs_Polar import Membrane_PINNs
import numpy as np
from Membrane_PINNs_Polar import animate_solution
import os


def main():
    # Paths housekeeping
    path_current_folder = os.path.dirname(os.path.abspath(__file__))
    path_model_parameters = "/".join([path_current_folder, "saved_model_parameters.pth"])
    os.makedirs("/".join([path_current_folder, "outputs"]), exist_ok=True)

    # recreate the model using trained parameters from file
    model = Membrane_PINNs(HL_dim=20)
    model.load_state_dict(torch.load(path_model_parameters))
    model.eval()

    # Set some inputs to the network
    rinitial, rfinal,  = 0.1, 1
    tinitial, tfinal = 0, 20
    theta_initial, theta_final = 0, 2*np.pi
    Nr, Ntheta, Nt = 30, 30, 30
    r, theta, t = model.get_input_tensors(rinitial, rfinal, theta_initial, theta_final, tinitial, tfinal, Nr, Ntheta, Nt)

    # compute output 
    xi = model.forward(r.view(-1,1), theta.view(-1,1), t.view(-1,1)) # convert tensors into column vectors
    xi_np = xi.detach().numpy() # convert xi into a np array
    xi_reshaped = xi_np.reshape(Nr,Ntheta,Nt) # reshape to fit dimentions

    # create plot for solution
    animate_solution(path_to_folder=path_current_folder, n_epochs=0,
                        xi=xi_reshaped, Nr=Nr, Ntheta=Ntheta, Nt=Nt, 
                        r_f=rfinal, r_i=rinitial, theta_f=theta_final, theta_i=theta_initial,
                        t_f=tfinal, t_i=tinitial, save_timesteps=True,
                        zlims=[-0.05, 0.05])


if __name__ == "__main__":
    main()