//===----- PowerPC64TargetValues.cpp - PowerPC64 specific value generator -----===//
//
//                     The LLVM Compiler Infrastructure
//
// This file is distributed under the University of Illinois Open Source
// License. See LICENSE.TXT for details.
//
//===----------------------------------------------------------------------===//

#include "llvm/Target/TargetValues.h"

namespace llvm {

class PowerPC64Values final : public TargetValues {
public:
  PowerPC64Values() {}
  virtual MachineLiveValPtr getMachineValue(const MachineInstr *MI) const;

private:
  void genADDInstructions(const MachineInstr *MI,
                          MachineGeneratedVal::ValueGenInstList &IL) const;
  void
  genBitfieldInstructions(const MachineInstr *MI,
                          MachineGeneratedVal::ValueGenInstList &IL) const;
};

}

