//
//  Analyzer.h
//  FreqAnalysis
//
//  Created by Markus Færevaag on 12.06.13.
//  Copyright (c) 2013 Markus Færevaag. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "Entry.h"

@interface Analyzer : NSObject

@property (readonly, copy) NSMutableArray *entries; // of FrequencyEntries

- (void) analyzeContent: (NSString *)content;

- (void) addEntry: (Entry *)entry;

@end
