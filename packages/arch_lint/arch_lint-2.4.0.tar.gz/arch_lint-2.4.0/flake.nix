{
  description = "Pure functional and typing utilities";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?rev=0cd51a933d91078775b300cf0f29aa3495231aa2";
    nix_filter.url = "github:numtide/nix-filter";
  };
  outputs = {
    self,
    nixpkgs,
    nix_filter,
  }: let
    system = "x86_64-linux";
    metadata = (builtins.fromTOML (builtins.readFile ./pyproject.toml)).project;
    path_filter = nix_filter.outputs.lib;
    src = path_filter {
      root = self;
      include = [
        "mypy.ini"
        "pyproject.toml"
        (path_filter.inDirectory metadata.name)
        (path_filter.inDirectory "mock_module")
        (path_filter.inDirectory "tests")
      ];
    };
    out = python_version:
      import ./build {
        inherit src python_version;
        nixpkgs = nixpkgs.legacyPackages."${system}";
      };
    supported = ["python38" "python39" "python310" "python311"];
    python_outs = builtins.listToAttrs (map (name: {
        inherit name;
        value = out name;
      })
      supported);
  in {
    packages."${system}" = python_outs;
    defaultPackage."${system}" = self.packages."${system}".python38.pkg;
  };
}
