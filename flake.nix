{
  description = "Example Python development environment for Zero to Nix";

  # Flake inputs
  inputs = {
    nixpkgs.url = "https://flakehub.com/f/NixOS/nixpkgs/0.2305.491812.tar.gz";
    #nixpkgs.url = "nixpkgs/nixos-unstable";
  };

  # Flake outputs
  outputs = { self, nixpkgs }:
    let
      # Systems supported
      allSystems = [
        "x86_64-linux" # 64-bit Intel/AMD Linux
        "aarch64-linux" # 64-bit ARM Linux
        "x86_64-darwin" # 64-bit Intel macOS
        "aarch64-darwin" # 64-bit ARM macOS
      ];

      # Helper to provide system-specific attributes
      forAllSystems = f: nixpkgs.lib.genAttrs allSystems (system: f {
        pkgs = import nixpkgs { inherit system; };
      });
    in
    {
      # Development environment output
      devShells = forAllSystems ({ pkgs }: {
        default =
          let
            # Use Python 3.10
            python = pkgs.python310;
          in
          pkgs.mkShell {
            # The Nix packages provided in the environment
            packages = [
              # Python plus helper tools
              (python.withPackages (ps: with ps; [
                virtualenv # Virtualenv
                pip # The pip installer
                black
                flake8
                mypy
                python-lsp-server
		pytest
                tkinter
              ]))
            ];
#            shellHook = ''
#            if [ -d "v-env" ]; then
#              echo "Skipping venv creation, 'v-env' already exists"
#            else
#              echo "Creating new venv environment in path: 'v-env'"
#              sleep 1
#              python -m venv "v-env"
#            fi
#            source "v-env/bin/activate"
#            pip install -r ./requirements.txt
#            '';
          };
      });
    };
}
