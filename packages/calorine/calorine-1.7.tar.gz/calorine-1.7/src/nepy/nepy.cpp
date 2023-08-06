#include "nepy.h"
#include "nep.cpp"
#include "nep.h"
#include <cmath>
#include <pybind11/iostream.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <unistd.h>

using namespace std;
namespace py = pybind11;

NEPY::NEPY(const std::string &potential_filename, int N_atoms,
           std::vector<double> cell, std::vector<std::string> atom_symbols,
           std::vector<double> positions, std::vector<double> masses)
    : nep(potential_filename), potential_filename(potential_filename) {
  /**
   @brief Wrapper class for NEP3 in nep.cpp.
   @details This class wraps the setup functionality of the NEP3 class in
   nep.cpp.
   @param potential_filename   Path to the NEP model (/path/nep.txt).
   @param N_atoms              The number of atoms in the structure.
   @param cell                 The cell vectors for the structure.
   @param atom_symbols         The atomic symbol for each atom in the structure.
   @param positions            The position for each atom in the structure.
   @param masses               The mass for each atom in the structure.
  */
  atom.N = N_atoms;
  atom.position = positions;
  atom.mass = masses;
  atom.cell = cell;
  atom.type.resize(atom.N);

  std::vector<std::string> model_atom_symbols =
      _getAtomSymbols(potential_filename); // load atom symbols used in model
  _convertAtomTypeNEPIndex(atom.N, atom_symbols, model_atom_symbols, atom.type);
}

std::vector<double> NEPY::getDescriptors() {
  /**
   @brief Get NEP descriptors.
   @details Calculates NEP descriptors for a given structure and NEP potential.
  */
  std::vector<double> descriptor(atom.N * nep.annmb.dim);
  nep.find_descriptor(atom.type, atom.cell, atom.position, descriptor);
  return descriptor;
}

std::vector<double> NEPY::getLatentSpace() {
  /**
   @brief Get the NEP latent space.
   @details Calculates the latent space of a NEP model, i.e., the activations
   after the first layer.
  */
  std::vector<double> latent(atom.N * nep.annmb.num_neurons1);
  nep.find_latent_space(atom.type, atom.cell, atom.position, latent);
  return latent;
}

std::vector<double> NEPY::getDipole() {
  /**
   @brief Get dipole.
   @details Calculates the dipole (a vector of length 3) for the whole box.
  */
  std::vector<double> dipole(3);
  nep.find_dipole(atom.type, atom.cell, atom.position, dipole);
  return dipole;
}

void NEPY::_getCenterOfMass(std::vector<double> center_of_mass) {
  /**
   @brief Computes the center of mass for current atoms object.
   @details Computes the center of mass (COM) for the structure with positions
   defined by atom.position. The COM will be written as a three vector, with
   in the order [x_component, y_component, z_component].
   @param center_of_mass      Vector to hold the center of mass.
  */

  double total_mass = 0.0;
  for (int i = 0; i < atom.N; i++) {
    // positions are in order [x1, ..., xN, y1, ..., yN, z1, ..., zN]
    center_of_mass[0] += atom.position[i] * atom.mass[i];
    center_of_mass[1] += atom.position[i + atom.N] * atom.mass[i];
    center_of_mass[2] += atom.position[i + 2 * atom.N] * atom.mass[i];
    total_mass += atom.mass[i];
  }
  center_of_mass[0] /= total_mass;
  center_of_mass[1] /= total_mass;
  center_of_mass[2] /= total_mass;
}

std::vector<double> NEPY::getDipoleGradient(double displacement, int method,
                                            double charge) {
  /**
   @brief Get dipole gradient through finite differences.
   @details Calculates the dipole gradient, a (N_atoms, 3, 3) tensor for the
   gradients dµ_k/dr_ij, for atom i, Cartesian direction j (x, y, z) and dipole
   moment component k. Mode is either forward difference (method=0) or central
   difference (method=1).
   Before computing the gradient the dipoles are corrected using the center of
   mass and the total system charge, supplied via the parameter `charge`.
   @param displacement        Displacement in Å.
   @param method              0 or 1, corresponding to forward or central
   differences.
   @param charge              Total system charge, used to correct dipoles.
  */

  std::vector<double> dipole_gradient(atom.N * 3 * 3);

  // Compute the total mass - need this for the corrections to COM
  double M = 0.0;
  for (int i = 0; i < atom.N; i++) {
    M += atom.mass[i];
  }

  if (method == 0) {
    // For forward differences we save the first dipole with no displacement
    std::vector<double> dipole(3);
    nep.find_dipole(atom.type, atom.cell, atom.position, dipole);

    // Correct original dipole
    std::vector<double> center_of_mass(3);
    _getCenterOfMass(center_of_mass);
    for (int i = 0; i < 3; i++) {
      dipole[i] += charge * center_of_mass[i];
    }

    // dipole vectors are zeroed in find_dipole, can be allocated here
    std::vector<double> dipole_forward(3);

    // Compute dipole for forward displacement
    const int N_cartesian = 3;
    const int values_per_atom = N_cartesian * N_cartesian;

    // Positions are in order [x1, ..., xN, y1, ..., yN, ...]
    int index = 0;
    double old_position = 0.0;
    double old_center_of_mass = 0.0;
    const double displacement_over_M = displacement / M;
    const double one_over_displacement = 1.0 / displacement;

    for (int i = 0; i < atom.N; i++) {
      for (int j = 0; j < N_cartesian; j++) {
        index = i + atom.N * j; // idx of position to change
        old_position = atom.position[index];
        atom.position[index] += displacement;
        // center of mass gest moved by +h/N*m_i in the same direction
        old_center_of_mass = center_of_mass[j];
        center_of_mass[j] += displacement_over_M * atom.mass[i];

        nep.find_dipole(atom.type, atom.cell, atom.position, dipole_forward);

        for (int k = 0; k < N_cartesian; k++) {
          dipole_gradient[i * values_per_atom + j * N_cartesian + k] =
              ((dipole_forward[k] + charge * center_of_mass[k]) - dipole[k]) *
              one_over_displacement;
        }
        // Restore positions
        atom.position[index] = old_position;
        center_of_mass[j] = old_center_of_mass;
      }
    }
  } else if (method == 1) {
    // For central differences we need both forwards and backwards displacements

    // Compute dipole for forward displacement
    const int N_cartesian = 3;
    const int values_per_atom = N_cartesian * N_cartesian;

    // dipole vectors are zeroed in find_dipole, can be allocated here
    std::vector<double> dipole_forward(3);
    std::vector<double> dipole_backward(3);

    // use center of mass to correct for permanent dipole
    std::vector<double> center_of_mass_forward(3);
    _getCenterOfMass(center_of_mass_forward);
    std::vector<double> center_of_mass_backward(center_of_mass_forward);

    // Positions are in order [x1, ..., xN, y1, ..., yN, ...]
    int index = 0;
    double old_position = 0.0;
    double old_center_of_mass = 0.0;
    const double displacement_over_M = displacement / M;
    const double one_over_two_displacements = 0.5 / displacement;

    for (int i = 0; i < atom.N; i++) {
      for (int j = 0; j < N_cartesian; j++) {
        index = i + atom.N * j; // idx of position to change
        old_position = atom.position[index];
        old_center_of_mass = center_of_mass_forward[j];

        // Forward displacement
        atom.position[index] += displacement;
        // center of mass gest moved by +h/N in the same direction
        center_of_mass_forward[j] += displacement_over_M * atom.mass[i];
        nep.find_dipole(atom.type, atom.cell, atom.position, dipole_forward);

        // Backwards displacement
        atom.position[index] -= 2 * displacement; // +h - 2h = -h
        center_of_mass_backward[j] -= displacement_over_M * atom.mass[i];
        nep.find_dipole(atom.type, atom.cell, atom.position, dipole_backward);

        for (int k = 0; k < N_cartesian; k++) {
          dipole_gradient[i * values_per_atom + j * N_cartesian + k] =
              ((dipole_forward[k] + charge * center_of_mass_forward[k]) -
               (dipole_backward[k] + charge * center_of_mass_backward[k])) *
              one_over_two_displacements;
        }
        // Restore positions
        atom.position[index] = old_position;
        center_of_mass_forward[j] = old_center_of_mass;
        center_of_mass_backward[j] = old_center_of_mass;
      }
    }
  }
  // dipole gradient component d_x refers to cartesian direction x
  // x1 refers to x position of atom 1
  // order: [dx_x1, dy_x1, dz_x1,
  //         dx_y1, dy_y1, dz_y1,
  //         dx_z1, dy_z1, dz_z1,
  //         ...
  //         dx_zN, dy_zN, dz_zN]
  return dipole_gradient;
}

std::tuple<std::vector<double>, std::vector<double>, std::vector<double>>
NEPY::getPotentialForcesAndVirials() {
  /**
   @brief Calculate potential, forces and virials.
   @details Calculates potential energy, forces and virials for a given
   structure and NEP potential.
  */
  std::vector<double> potential(atom.N);
  std::vector<double> force(atom.N * 3);
  std::vector<double> virial(atom.N * 9);
  nep.compute(atom.type, atom.cell, atom.position, potential, force, virial);
  return std::make_tuple(potential, force, virial);
}

std::vector<std::string> NEPY::_getAtomSymbols(std::string potential_filename) {
  /**
   @brief Fetches atomic symbols
   @details This function fetches the atomic symbols from the header of a NEP
   model. These are later used to ensure consistent indices for the atom types.
   @param potential_filename Path to the NEP model (/path/nep.txt).
   */
  std::ifstream input_potential(potential_filename);
  if (!input_potential.is_open()) {
    std::cout << "Error: cannot open nep.txt.\n";
    exit(1);
  }
  std::string potential_name;
  input_potential >> potential_name;
  int number_of_types;
  input_potential >> number_of_types;
  std::vector<std::string> atom_symbols(number_of_types);
  for (int n = 0; n < number_of_types; ++n) {
    input_potential >> atom_symbols[n];
  }
  input_potential.close();
  return atom_symbols;
}

void NEPY::_convertAtomTypeNEPIndex(int N,
                                    std::vector<std::string> atom_symbols,
                                    std::vector<std::string> model_atom_symbols,
                                    std::vector<int> &type) {
  /**
   @brief Converts atom species to NEP index.
   @details Converts atomic species to indicies, which are used in NEP.
   @param atom_symbols        List of atom symbols.
   @param model_atom_symbols  List of atom symbols used in the model.
   @param type                List of indices corresponding to atom type.
  */
  for (int n = 0; n < N; n++) {
    // Convert atom type to index for consistency with nep.txt
    // (potential_filename)
    std::string atom_symbol = atom_symbols[n];
    bool is_allowed_element = false;
    for (int t = 0; (unsigned)t < model_atom_symbols.size(); ++t) {
      if (atom_symbol == model_atom_symbols[t]) {
        type[n] = t;
        is_allowed_element = true;
      }
    }
    if (!is_allowed_element) {
      std::cout << "Error: Atom type " << atom_symbols[n]
                << " not used in the given NEP potential.\n";
      exit(1);
    }
  }
}

void NEPY::setPositions(std::vector<double> positions) {
  /**
   @brief Sets positions.
   @details Sets the positions of the atoms object.
   Also updates the center of mass.
   @param positions           List of positions.
  */
  for (int i = 0; i < atom.N * 3; i++) {
    atom.position[i] = positions[i];
  }
}

void NEPY::setCell(std::vector<double> cell) {
  /**
   @brief Sets cell.
   @details Sets the cell of the atoms object.
   @param Cell                Cell vectors.
  */
  for (int i = 0; i < 9; i++) {
    atom.cell[i] = cell[i];
  }
}

void NEPY::setMasses(std::vector<double> masses) {
  /**
   @brief Sets masses.
   @details Sets the masses of the atoms object.
   @param Cell                Atom masses.
  */
  for (int i = 0; i < atom.N; i++) {
    atom.mass[i] = masses[i];
  }
}

void NEPY::setSymbols(std::vector<std::string> atom_symbols) {
  /**
   @brief Sets symbols.
   @details Sets the symbols of the atoms object from the ones used in the
   model.
   @param atom_symbols        List of symbols.
  */
  std::vector<std::string> model_atom_symbols =
      _getAtomSymbols(potential_filename); // load atom symbols used in model
  _convertAtomTypeNEPIndex(atom.N, atom_symbols, model_atom_symbols, atom.type);
}

PYBIND11_MODULE(_nepy, m) {
  m.doc() = "Pybind11 interface for NEP";
  py::class_<NEPY>(m, "NEPY")
      .def(py::init<const std::string &, int, std::vector<double>,
                    std::vector<std::string>, std::vector<double>,
                    std::vector<double>>(),
           py::arg("potential_filename"), py::arg("N_atoms"), py::arg("cell"),
           py::arg("atom_symbols"), py::arg("positions"), py::arg("masses"),
           py::call_guard<py::scoped_ostream_redirect,
                          py::scoped_estream_redirect>())
      .def("set_positions", &NEPY::setPositions, "Set atom positions",
           py::arg("positions"))
      .def("set_cell", &NEPY::setCell, "Set cell", py::arg("cell"))
      .def("set_masses", &NEPY::setMasses, "Set masses", py::arg("masses"))
      .def("set_symbols", &NEPY::setSymbols, "Set atom symbols",
           py::arg("atom_symbols"))
      .def("get_descriptors", &NEPY::getDescriptors, "Get descriptors")
      .def("get_dipole", &NEPY::getDipole, "Get dipole")
      .def("get_dipole_gradient", &NEPY::getDipoleGradient, "Get dipole",
           py::arg("displacement"), py::arg("method"), py::arg("charge"))
      .def("get_latent_space", &NEPY::getLatentSpace, "Get latent space")
      .def("get_potential_forces_and_virials",
           &NEPY::getPotentialForcesAndVirials,
           "Get potential, forces and virials");
}
