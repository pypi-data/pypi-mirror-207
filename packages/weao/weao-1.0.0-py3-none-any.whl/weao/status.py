from typing import Tuple, Dict

from .exploit import (Synapse, ScriptWare, Krnl, Dx9Ware, Electron, WeAreDevs, OxygenU, Fluxus, Celestial, Comet, Elexe, Roblox)

class Status:
    """
    Class Interface Containing User Attributes

    Attributes
    ----------
    synapse: :class:Synapse
        Synapse Exploit Status
    script_ware: :class:ScriptWare
        Script Ware Exploit Status
    krnl: :class:Krnl
        KRNL Exploit Status
    dx9ware: :class:Dx9Ware
        DX9WARE Exploit Status
    electron: :class:Electron
        Electron Exploit Status
    wearedevs_api: :class:WeAreDevs
        We Are Devs API Exploit Status
    oxygen: :class:OxygenU
        Oxygen-U Exploit Status
    fluxus: :class:Fluxus
        Fluxus Exploit Status
    celestial: :class:Celestial
        Celestial Exploit Status
    comet: :class:Comet
        Comet Exploit Status
    elexe: :class:Elexe
        Elexe Exploit Status
    roblox: :class:Roblox
        ROBLOX Exploit Status
    """
    __slots__: Tuple[str, ...] = (
        "synapse",
        "script_ware",
        "krnl",
        "dx9ware",
        "electron",
        "wearedevs_api",
        "oxygen",
        "fluxus",
        "celestial",
        "comet",
        "elexe",
        "roblox",
    )

    def __init__(self, data: Dict) -> None:
        self.synapse = Synapse(data[0].get("Synapse"))
        self.script_ware = ScriptWare(data[1].get("Script-Ware"))
        self.krnl = Krnl(data[2].get("KRNL"))
        self.dx9ware = Dx9Ware(data[3].get("DX9WARE"))
        self.electron = Electron(data[4].get("Electron"))
        self.wearedevs_api = WeAreDevs(data[5].get("WeAreDevs API"))
        self.oxygen = OxygenU(data[6].get("Oxygen-U"))
        self.fluxus = Fluxus(data[7].get("Fluxus"))
        self.celestial = Celestial(data[8].get("Celestial"))
        self.comet = Comet(data[9].get("Comet"))
        self.elexe = Elexe(data[10].get("Elexe"))
        self.roblox = Roblox(data[11].get("ROBLOX"))

    def __repr__(self) -> str:
        return "<Status>"
    
