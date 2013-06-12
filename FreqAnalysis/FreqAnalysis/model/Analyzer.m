//
//  Analyzer.m
//  FreqAnalysis
//
//  Created by Markus Færevaag on 12.06.13.
//  Copyright (c) 2013 Markus Færevaag. All rights reserved.
//

#import "Analyzer.h"

@interface Analyzer ()
@property (readwrite, copy) NSMutableArray *entries;

@end

@implementation Analyzer

@synthesize entries;

- (void) analyzeContent:(NSString *)content
{
    NSLog(@"ANALyze");
}

- (void) addEntry: (Entry *)entry
{
    [self.entries addObject:entry];
}

@end
