//
//  MainViewController.m
//  FreqAnalysis
//
//  Created by Markus Færevaag on 12.06.13.
//  Copyright (c) 2013 Markus Færevaag. All rights reserved.
//

#import "MainViewController.h"
#import "Analyzer.h"
#import "Entry.h"

#define CYPHERTEXT_FILE @"Text"

@interface MainViewController ()
@property (copy) NSString *text;
@property Analyzer *freqAnalyzer;

@property (weak) IBOutlet NSProgressIndicator *progIndicator;
@property (weak) IBOutlet NSTableView *table;

@end

@implementation MainViewController

@synthesize freqAnalyzer, text, progIndicator, table = _table;

- (IBAction)analyze:(id)sender
{
    if (!self.text) {
        NSString *path = [[NSBundle mainBundle] pathForResource:CYPHERTEXT_FILE
                                                         ofType:@"txt"];
        self.text = [NSString stringWithContentsOfFile:path
                                              encoding:NSUTF8StringEncoding
                                                 error:NULL];
    }
    
    [self.progIndicator setHidden:NO];
    [self.progIndicator startAnimation:nil];
    [sender setEnabled:NO];
    dispatch_queue_t queue = dispatch_queue_create("queue", 0);
    dispatch_async(queue, ^{
        
        [self.freqAnalyzer analyzeContent:self.text];
        
        // Fire UI commands in main thread
        dispatch_sync(dispatch_get_main_queue(), ^{
            [self.progIndicator setHidden:YES];
            [self.progIndicator stopAnimation:nil];
            [sender setEnabled:YES];
            NSLog(@"RELOAD");
            [_table reloadData];
        });
    });
}

- (NSInteger) numberOfRowsInTableView: (NSTableView *)tableView
{
    NSLog(@"HELLO ROWS");
    return [self.freqAnalyzer.entries count];
}

- (NSView *) tableView: (NSTableView *)tableView
    viewForTableColumn: (NSTableColumn *)tableColumn
                   row: (NSInteger)row
{
    
    NSString *key = [[self.freqAnalyzer.entries allKeys] objectAtIndex:row];
    Entry *entry = [self.freqAnalyzer.entries objectForKey:key];
    
    NSLog(@"HELLO");
    NSLog(@"%@", tableColumn.value);
    
    NSString *identifier = [tableColumn identifier];
    NSTextField *textField = [tableView makeViewWithIdentifier:identifier owner:self];
    
    if ([identifier isEqualToString:@"Value"]) {
        textField.objectValue = entry.value;
    } else if ([identifier isEqualToString:@"Type"]) {
        textField.objectValue = [Entry typeToString:entry.type];
    } else if ([identifier isEqualToString:@"Occurences"]) {
        textField.objectValue = [NSString stringWithFormat:@"%lu", (unsigned long)entry.occurences];
    } else if ([identifier isEqualToString:@"Frequency"]) {
        textField.objectValue = entry.frequency;
    }
    
    return textField;
}

@end
