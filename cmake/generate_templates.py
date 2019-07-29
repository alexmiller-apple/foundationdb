#!/usr/bin/env python

import json
import optparse
import filecmp
import os
import shutil


class InternalError(Exception):
    pass


class TemplateGenerator(object):
    def __init__(self, args):
        self.targetName = args.target
        self.numFiles = args.num_files
        self.fileName = args.out
        with open(args.file, 'r') as f:
            self.descr = json.load(f)

    def generate(self):
        target = self.descr.get(self.targetName, {})
        dependencies = []
        for dep in target['dependencies'] if 'dependencies' in target else []:
            if dep not in self.descr:
                print("ERROR: %s was declared as dependency of %s but does not exist"%(dep, self.targetName))
                raise InternalError
            dependencies.append((dep, self.descr[dep]))
        for i in range(0, self.numFiles):
            outFile = "%s%d.cpp"%(self.fileName, i)
            tmpFile = "%s.tmp"%(outFile,)
            with open(tmpFile, 'w') as f:
                f.write('// This file was generated - DO NOT CHANGE\n\n')
                for include in target["includes"] if 'includes' in target else []:
                    f.write('#include "%s"\n'%(include,))
                for include in target["sysincludes"] if 'sysincludes' in target else []:
                    f.write('#include <%s>\n'%(include,))
                j = 0
                f.write('\n\n\n')
                templates = target['templates'] if 'templates' in target else []
                templates.sort()
                for template in templates:
                    for dep in dependencies:
                        ts = dep[1]['templates'] if 'templates' in dep[1] else []
                        if template in ts:
                            print("ERROR: %s is also defined in %s which is a dependency"%(template, dep[0]))
                            raise InternalError
                    if j % self.numFiles == i:
                        f.write('template struct %s;\n'%(template,))
                    j += 1
            # Compiling these files will be quite expensive. So we make sure to only
            # write them if they have changed
            if (not os.path.exists(outFile)) or (not filecmp.cmp(outFile, tmpFile)):
                shutil.copyfile(tmpFile, outFile)

if __name__ == '__main__':
    parser = optparse.OptionParser(description="Generate explicit template specification")
    parser.add_option('-N', '--num-files', type=int, default=8)
    parser.add_option('-o', '--out', type=str, default="SerializeImpl")
    parser.add_option('-t', '--target', type=str)
    options, args = parser.parse_args()
    options.file = args[0]
    generator = TemplateGenerator(options)
    generator.generate()
